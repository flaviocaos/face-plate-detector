
# Detecção de Faces e Placas com Desfoque

Este projeto realiza a detecção de rostos e placas em imagens veiculares e aplica desfoque para anonimização.

## Estrutura

- processa_faces.py: Código principal para processamento em batch.
- deteccao_faces_entulho.ipynb: Notebook para execução interativa.
- requirements.txt: Dependências Python.
- .gitignore: Arquivos e pastas ignorados pelo Git.

## Como usar

1. Configure os caminhos dos modelos no `processa_faces.py`.
2. Ajuste as pastas de entrada e saída de imagens.
3. Crie ambiente virtual e instale dependências:
   ```bash
   python3 -m venv gaia-env
   source gaia-env/bin/activate
   pip install -r requirements.txt
   ```
4. Execute o script ou use o notebook.

## Autor

Flavio Antonio Oliveira da Silva
