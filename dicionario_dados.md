
# 📘 Dicionário de Dados

## 🔷 1. Inputs

| Nome do Dado       | Tipo/Formato                         | Descrição                                                                 |
|--------------------|--------------------------------------|---------------------------------------------------------------------------|
| Imagens originais  | `.jpg`, `.png`, `.bmp`, entre outros | Arquivos de imagem a serem processados para anonimização.                |
| Modelos TensorFlow | `.pb`                                | Arquivos de pesos pré-treinados para detecção de rostos e placas veiculares. |

---

## 🔶 2. Outputs

| Nome do Dado          | Tipo/Formato                         | Descrição                                                                 |
|------------------------|--------------------------------------|---------------------------------------------------------------------------|
| Imagens anonimizadas   | Igual ao formato da imagem original  | Imagens com regiões sensíveis (rostos e placas) desfocadas para anonimização. |

---

## ⚙️ 3. Parâmetros Configuráveis

| Parâmetro           | Tipo        | Valor Padrão  | Descrição                                                                 |
|---------------------|-------------|----------------|---------------------------------------------------------------------------|
| `FACE_THRESHOLD`    | `float`     | 0.5            | Limite mínimo de confiança para detecção de rostos.                      |
| `PLATE_THRESHOLD`   | `float`     | 0.5            | Limite mínimo de confiança para detecção de placas veiculares.          |
| `OBFUSCATION_KERNEL`| `tuple(int)`| (201, 201)     | Tamanho do kernel utilizado no filtro de desfoque (blur).               |
| `JPEG_QUALITY`      | `int`       | 75             | Qualidade da imagem de saída, quando salva como JPEG (0-100).            |
