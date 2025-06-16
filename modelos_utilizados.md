# Modelos de IA Utilizados – Projeto: Detecção e Desfoque de Rostos e Placas

Este documento descreve os modelos de aprendizado profundo (Deep Learning) utilizados no pipeline de detecção e anonimização de rostos e placas veiculares.

---

## 🧠 1. Modelo de Detecção de Rostos

- **Nome do arquivo:** `weights_face_v1.0.0.pb`
- **Tipo:** TensorFlow Frozen Graph (.pb)
- **Framework:** TensorFlow 1.x (compatível com `tf.compat.v1`)
- **Entrada esperada:** Imagem RGB (qualquer resolução)
- **Saída:** 
  - `detection_boxes`: coordenadas normalizadas dos rostos
  - `detection_scores`: confiança da detecção
- **Threshold de confiança:** 0.5
- **Função no pipeline:** Detectar rostos em imagens panorâmicas veiculares para posterior desfoque por `cv2.GaussianBlur`.

---

## 🚗 2. Modelo de Detecção de Placas

- **Nome do arquivo:** `weights_plate_v1.0.0.pb`
- **Tipo:** TensorFlow Frozen Graph (.pb)
- **Framework:** TensorFlow 1.x
- **Entrada esperada:** Imagem RGB
- **Saída:**
  - `detection_boxes`: coordenadas das regiões de placas
  - `detection_scores`: scores das detecções
- **Threshold de confiança:** 0.5
- **Função no pipeline:** Detectar placas veiculares e aplicar anonimização por desfoque para atender exigências de privacidade.

---

## 🗂 Estrutura de Caminhos Utilizados

```python
FACE_MODEL_PATH = "flavio/models/weights_face_v1.0.0.pb"
PLATE_MODEL_PATH = "flavio/models/weights_plate_v1.0.0.pb"
```

Os modelos são carregados com a função:

```python
def load_frozen_graph(pb_file_path):
    with tf.io.gfile.GFile(pb_file_path, "rb") as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
    graph = tf.Graph()
    with graph.as_default():
        tf.import_graph_def(graph_def, name="")
    return graph
```

---

## 📌 Observações

- Ambos os modelos foram otimizados para rodar em CPU e não dependem de CUDA.
- O pipeline está configurado para tolerar ROIs pequenas demais para desfoque, com `logging.warning` e `continue`.
- Foi aplicada Non-Max Suppression (NMS) para evitar sobreposição de detecções.
- O desfoque é aplicado 3 vezes sequencialmente com kernel `(251, 251)` para garantir alta anonimização visual.
- Os arquivos `.pb` estão organizados no repositório em:  
  `/flavio/models/`

---
