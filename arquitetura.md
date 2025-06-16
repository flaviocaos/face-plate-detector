
# 🏗️ Arquitetura do Sistema

- O script principal (`processa_faces.py`) utiliza TensorFlow para detecção.
- Utiliza OpenCV para processamento das imagens (desfoque, leitura, escrita).
- Usa `logging` para monitorar o processo.
- Arquitetura modular para permitir fácil substituição de modelos.
- Compatível com execução em Linux e Windows via WSL.

## 🧠 Modelos

- `weights_face_v1.0.0.pb`: Modelo TensorFlow para detecção de rostos.
- `weights_plate_v1.0.0.pb`: Modelo TensorFlow para detecção de placas veiculares.
