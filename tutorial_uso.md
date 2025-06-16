
# 📖 Tutorial de Uso

## 🔧 Preparação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Configure o ambiente virtual Python e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate   # Windows

   pip install -r requirements.txt
   ```

3. Ajuste os caminhos no arquivo `processa_faces.py` conforme necessário para:
   - Pasta de entrada e saída de imagens
   - Caminhos dos modelos `.pb`
   - Parâmetros opcionais (thresholds, qualidade, kernel)

## ▶️ Execução

Execute o script com:
```bash
python processa_faces.py
```
