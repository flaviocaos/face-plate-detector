import os
import cv2
import numpy as np
import tensorflow as tf
from tqdm import tqdm
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
tf.compat.v1.disable_eager_execution()

FACE_MODEL_PATH = 'flavio/models/weights_face_v1.0.0.pb'
INPUT_BASE_FOLDER = "/mnt/cadastro/br/sc/balneario_camboriu/fotos_veiculares/panoramica/PM_BAL_CAMB_20230920__ORIGINAL"
OUTPUT_BASE_FOLDER = "/mnt/data/flavio_faces"
PROCESSED_LOG = os.path.join(OUTPUT_BASE_FOLDER, 'imagens_processadas_faces.txt')

FACE_THRESHOLD = 0.5
OBFUSCATION_KERNEL = (251, 251)
JPEG_QUALITY = 75
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')

def load_frozen_graph(pb_file_path):
    with tf.io.gfile.GFile(pb_file_path, "rb") as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
    graph = tf.Graph()
    with graph.as_default():
        tf.import_graph_def(graph_def, name="")
    return graph

face_graph = load_frozen_graph(FACE_MODEL_PATH)
face_sess = tf.compat.v1.Session(graph=face_graph)
face_input_tensor = face_graph.get_tensor_by_name("image_tensor:0")
face_boxes_tensor = face_graph.get_tensor_by_name("detection_boxes:0")
face_scores_tensor = face_graph.get_tensor_by_name("detection_scores:0")

def detect_faces(sess, image, threshold=0.5):
    img_expanded = np.expand_dims(image, axis=0)
    boxes, scores = sess.run([face_boxes_tensor, face_scores_tensor], feed_dict={face_input_tensor: img_expanded})
    boxes = np.squeeze(boxes)
    scores = np.squeeze(scores)
    detections = []
    h, w, _ = image.shape
    for i, score in enumerate(scores):
        if score >= threshold:
            ymin, xmin, ymax, xmax = boxes[i]
            x1 = int(xmin * w)
            y1 = int(ymin * h)
            x2 = int(xmax * w)
            y2 = int(ymax * h)
            detections.append((x1, y1, x2, y2, score))
    return detections

def blur_regions(image, detections, kernel_size=(251, 251)):
    processed_image = image.copy()
    for (x1, y1, x2, y2, score) in detections:
        roi = processed_image[y1:y2, x1:x2]
        k_h, k_w = kernel_size
        roi = cv2.GaussianBlur(roi, (k_w | 1, k_h | 1), 0)
        processed_image[y1:y2, x1:x2] = roi
    return processed_image

if not os.path.exists(OUTPUT_BASE_FOLDER):
    os.makedirs(OUTPUT_BASE_FOLDER)

processed = set()
if os.path.exists(PROCESSED_LOG):
    with open(PROCESSED_LOG, 'r') as f:
        processed = set(line.strip() for line in f)

for root, _, files in os.walk(INPUT_BASE_FOLDER):
    rel_path = os.path.relpath(root, INPUT_BASE_FOLDER)
    output_dir = os.path.join(OUTPUT_BASE_FOLDER, rel_path)
    os.makedirs(output_dir, exist_ok=True)
    for file in files:
        if not file.lower().endswith(IMAGE_EXTENSIONS) or file in processed:
            continue
        input_path = os.path.join(root, file)
        output_path = os.path.join(output_dir, file)
        try:
            image = cv2.imread(input_path)
            detections = detect_faces(face_sess, image, FACE_THRESHOLD)
            result = blur_regions(image, detections) if detections else image
            cv2.imwrite(output_path, result, [cv2.IMWRITE_JPEG_QUALITY, JPEG_QUALITY])
            with open(PROCESSED_LOG, 'a') as f:
                f.write(file + '\n')
        except Exception as e:
            logging.error(f"Erro ao processar {file}: {e}")
face_sess.close()
