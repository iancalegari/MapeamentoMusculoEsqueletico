# Projeto A3 - Mapeamento Músculo Esquelético. 

**Sobre:** Neste projeto foi desenvolvido um sistema interativo que utiliza visão computacional para detectar partes do corpo humano em tempo real. Ao aproximar a mão de uma região específica do corpo, o sistema reconhece a interação e exibe vídeos explicativos relacionados a essa área.

O sistema inclui:
- Captura de vídeo ao vivo com detecção de pose humana usando a biblioteca CvZone.
- Identificação automática dos principais pontos do corpo para mapear regiões como cabeça, tronco, joelhos, entre outras.
- Associação de cada parte do corpo a vídeos informativos que são exibidos automaticamente quando a área é selecionada.
- Interface visual que destaca a parte do corpo selecionada e reproduz os vídeos de forma integrada.

As tecnologias utilizadas são Python, OpenCV para processamento de vídeo e CvZone para detecção de pose utilizando PoseModule e PoseDetector

## Requisitos para Execução:
 - Python 3.11.0
 - Use o app Camo Studio para conectar a câmera do celular ao PC.
     - Recomendações para o Camo Studio:
     - Use o celular na vertical (modo retrato).
     - Nas configurações do Camo Studio, defina a resolução para 1296x2304 a 30 FPS.
       
- Pacotes Python Necessários:
     - opencv-python==4.9.0.80
     - cvzone==1.5.6
     - pip install opencv-python cvzone numpy mediapipe
