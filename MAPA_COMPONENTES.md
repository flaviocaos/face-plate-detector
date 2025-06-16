# 🧭 Mapa de Componentes do Projeto

Este documento descreve os principais arquivos e diretórios do projeto **gaia-coleta360-detecao-desfoque**, explicando suas funções.

---

## 📁 Estrutura Principal

```
.
├── main.py                       # (ou notebook principal) Script principal de execução do pipeline
├── flavio/models/               # Modelos TensorFlow (.pb) de detecção de rosto e placa
├── imagens_processadas/         # Pasta onde as imagens com desfoque são salvas
├── /mnt/cadastro/.../ORIGINAL/  # Pasta com imagens panorâmicas originais
├── requirements.txt             # Lista de dependências Python para o projeto
├── arquitetura.md               # Diagrama e descrição da arquitetura da aplicação
├── fluxo_trabalho.md            # Explicação passo-a-passo do pipeline de execução
├── dicionario_dados.md          # Dicionário de dados com campos de entrada e saída
├── tutorial_uso.md              # Guia prático de como rodar o projeto
├── .github/workflows/           # CI/CD (GitHub Actions)
│   └── blank.yml                # Workflow de teste/execução (automatização)
```

---

## 🧠 Modelos Utilizados

| Caminho                        | Tipo                        | Descrição                                         |
|-------------------------------|-----------------------------|---------------------------------------------------|
| `flavio/models/weights_face_v1.0.0.pb`  | Modelo TensorFlow         | Detecção de rostos frontais em imagens panorâmicas |
| `flavio/models/weights_plate_v1.0.0.pb` | Modelo TensorFlow         | Detecção de placas de veículos                     |

---

## 🧪 Scripts e Funções Principais

- `load_frozen_graph()`: Carrega os modelos `.pb` para a memória.
- `detect_objects()`: Aplica detecção com TensorFlow.
- `blur_regions()`: Aplica desfoque com `cv2.GaussianBlur`.
- `non_max_suppression()`: Reduz sobreposições entre detecções.
- `process_and_save_image()`: Pipeline completo de leitura, detecção, desfoque e salvamento.

---

## 📝 Observações

- O projeto roda sobre imagens no formato `.jpg`, `.png` etc.
- Os parâmetros de desfoque, limiares de confiança e qualidade JPEG podem ser ajustados no topo do script.
- Sessões do TensorFlow são fechadas ao final do processamento para liberação de recursos.

---

Este mapa deve ser mantido atualizado conforme novos componentes forem adicionados ao repositório.
