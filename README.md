# Detecção de Rostos e Placas

## Visão Geral

Este projeto automatiza a detecção e anonimização de rostos e placas veiculares em imagens digitais, utilizando modelos treinados em TensorFlow. A solução permite o processamento em lote de grandes volumes de imagens, aplicando desfoque intenso para garantir a privacidade e conformidade com legislações como LGPD e GDPR.

## Motivação

Com o aumento das regulamentações de proteção de dados pessoais, a anonimização de imagens que contenham informações sensíveis tornou-se mandatória em muitos setores, incluindo segurança pública, mobilidade urbana e monitoramento veicular. Este projeto oferece uma ferramenta robusta para auxiliar empresas a cumprir tais normativas, preservando a identidade e dados pessoais de forma automatizada.

## Funcionalidades

- Detecção automática de rostos humanos e placas veiculares em imagens.
- Aplicação de desfoque configurável para anonimização eficaz.
- Processamento recursivo de diretórios, mantendo a estrutura original na saída.
- Registro detalhado do processamento via logs configuráveis.
- Fácil parametrização dos limiares de detecção e qualidade das imagens geradas.
- Compatível com ambientes Linux e Windows via WSL.

## Tecnologias Utilizadas

- **Python 3.11**: Linguagem de programação principal.
- **TensorFlow 2.x**: Framework para carregamento e execução dos modelos de detecção.
- **OpenCV**: Biblioteca para processamento de imagens.
- **TQDM**: Barra de progresso para acompanhamento do processamento.
- **GitHub Actions**: Integração contínua para testes automatizados e verificação de qualidade do código.

## Requisitos

- Python 3.11 ou superior instalado.
- Dependências descritas no arquivo `requirements.txt`.

## Instalação

Clone o repositório e configure o ambiente virtual:

git clone https://github.com/empresa/face-plate-detector.git
cd face-plate-detector
python3 -m venv env
source env/bin/activate      # Linux/macOS
.\env\Scripts\activate       # Windows PowerShell
pip install --upgrade pip
pip install -r requirements.txt

## Estrutura do projeto

Detecção de Rostos e Placas

- ├── processa_faces.py # Script principal de processamento
- ├── notebooks/ # Jupyter notebooks de análise e testes
- │ └── face_plate_detection.ipynb
- ├── models/ # Modelos TensorFlow (.pb)
- │ ├── weights_face_v1.0.0.pb
- │ └── weights_plate_v1.0.0.pb
- ├── images/ # Imagens originais para processamento
- ├── output/ # Imagens anonimizadas geradas
- ├── requirements.txt # Dependências do Python
- ├── .github/workflows/ # Workflows GitHub Actions para CI/CD
- │ └── python-ci.yml
- ├── docs/ # Documentação adicional
- │ ├── dicionario_dados.pdf
- │ └── fluxo_trabalho.pdf
- └── README.md # Documentação principal

## Como Utilizar

1. Configure os caminhos das pastas e arquivos no processa_faces.py.
2. Prepare seu ambiente virtual Python com as dependências em requirements.txt.
3. Execute o script para processar as imagens da pasta de entrada.
4. Confira as imagens processadas na pasta de saída configurada.

## Pré-requisitos

- Python 3.10 ou superior instalado
- Ambiente virtual configurado (recomendado)
- Dependências instaladas via `pip install -r requirements.txt`
- Modelos TensorFlow `.pb` localizados na pasta `models/`

## Parâmetros Ajustáveis

1. FACE_THRESHOLD e PLATE_THRESHOLD: Limiares de confiança para detecção (default 0.5)
2. OBFUSCATION_KERNEL: Tamanho do kernel do desfoque Gaussiano (ex: (201,201) para desfoque mais forte)
3. JPEG_QUALITY: Qualidade das imagens salvas (default 75)
4. Ajuste esses parâmetros conforme a necessidade para balancear qualidade de anonimização e preservação de detalhes.

## Executando o Script

python processa_faces.py

## Workflow de Desenvolvimento

1. Primeiro, teste com um pequeno subconjunto de imagens para ajustar limiares e desfoque.
2. Após validação, processe o conjunto completo.
3. Implemente testes unitários e de integração (pasta tests/).
4. Utilize o GitHub Actions para integração contínua e automação do deploy.

## Logs e Monitoramento

- O sistema gera logs detalhados com:
- Informações de imagens processadas
- Quantidade de rostos e placas detectados
- Avisos sobre regiões pequenas ou problemas durante o processamento
- Os logs são configurados para exibir data, hora e nível da mensagem.

## Documentação Complementar

- No diretório docs/ você encontra:
- Dicionário de Dados: Descrição das entradas, saídas e formatos utilizados
- Fluxo de Trabalho: Diagrama do processo completo de detecção e anonimização
- Outros documentos auxiliares para facilitar manutenção e expansão do projeto






