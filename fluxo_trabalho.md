
# 🔄 Fluxo de Trabalho

1. **Leitura das imagens** na pasta de entrada.
2. **Carregamento dos modelos TensorFlow** pré-treinados para rostos e placas.
3. **Detecção das regiões** com rostos e placas com base nos limiares configurados.
4. **Aplicação do desfoque Gaussiano** nas regiões detectadas.
5. **Salvamento das imagens anonimizadas** na pasta de saída, preservando a estrutura de pastas.
6. **Registro dos logs detalhados** para monitoramento e auditoria.
