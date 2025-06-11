# Detecção de Faces e Placas com Desfoque

Projeto em Python que detecta rostos e placas em imagens veiculares e aplica desfoque para anonimização. Utiliza TensorFlow e OpenCV para processar grandes volumes de imagens, garantindo privacidade e segurança, com suporte a execução via script e notebook interativo.

## Instalação

1. Crie e ative o ambiente virtual:

```bash
python3 -m venv gaia-env
source gaia-env/bin/activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Uso

- Configure os caminhos dos modelos no arquivo `processa_faces.py`.
- Ajuste as pastas de entrada e saída no mesmo arquivo.
- Execute o script:

```bash
python processa_faces.py
```

- Ou use o notebook `deteccao_faces_entulho.ipynb` para execução interativa.

## Estrutura do projeto

- `processa_faces.py`: Código principal para processamento.
- `deteccao_faces_entulho.ipynb`: Notebook com exemplo de uso.
- `requirements.txt`: Dependências do projeto.
- `.gitignore`: Arquivos ignorados pelo git.

## Como contribuir

1. Fork o repositório.
2. Crie uma branch com sua feature: `git checkout -b minha-feature`
3. Commit suas mudanças: `git commit -m "Minha nova feature"`
4. Push para sua branch: `git push origin minha-feature`
5. Abra um Pull Request.

## Autor

Flavio Antonio Oliveira da Silva

