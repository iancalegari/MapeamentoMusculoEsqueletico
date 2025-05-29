# A3 2025 - MAPEAMENTO MÚSCULO-ESQUELÉTICO

# CERTIFIQUE - SE DE UTILIZAR O CELULAR NA VERTICAL E NO APP DO CAMO STUDIO ( CAMERA DO CELULAR CONECTADO NO PC A RESOLUÇÃO ESTAR EM 1296X2304 A 30 FPS)
# COM A MÃO DIREITA TOQUE NOS PONTOS DO CORPO SELECIONADOS PARA EXIBIR O ESQUELETO E MUSCULATURA
# APERTE "q" para fechar

import cv2
import math
import os
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture(0)
pose_detector = PoseDetector()
background = cv2.imread('background1.png') #background é azul e background 1 é preto
background = cv2.resize(background, (1920, 1080))  

limite_distancia = 50
parte_selecionada = None
videos = {}  

# Mapeamento dos nomes das partes para cada arquivos de vídeo
mapeamento_videos = {
    "Cabeca": ["videos/cabecaEsq.mp4", "videos/cabecaMusc.mp4"],
    "Tronco": ["videos/peitoEsq.mp4", "videos/peitoMusc.mp4"],
    "Barriga": ["videos/barrigaEsq.mp4", "videos/barrigaMusc.mp4"],
    "Quadril": ["videos/membroinf1Esq.mp4", "videos/membroinf1Musc.mp4"],
    "Joelho Direito": ["videos/membroinf2Esq.mp4", "videos/membroinf2Musc.mp4"],
    "Joelho Esquerdo": ["videos/membroinf2Esq.mp4", "videos/membroinf2Musc.mp4"],
    "Pe Direito": ["videos/membroinf3Esq.mp4", "videos/membroinf3Musc.mp4"],
    "Pe Esquerdo": ["videos/membroinf3Esq.mp4", "videos/membroinf3Musc.mp4"]
}

def distancia(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def obter_pontos(lmList):
    centros = {}
    try: centros["Cabeca"] = (lmList[0][0], lmList[0][1])
    except: pass
    try: centros["Tronco"] = ((lmList[11][0]+lmList[12][0])//2, (lmList[11][1]+lmList[12][1])//2)
    except: pass
    try:
        centros["Barriga"] = ((lmList[11][0] + lmList[12][0] + lmList[23][0] + lmList[24][0]) // 4,
                              ((lmList[11][1] + lmList[12][1] + lmList[23][1] + lmList[24][1]) // 4) + 50)
    except: pass
    try: centros["Quadril"] = ((lmList[23][0]+lmList[24][0])//2, (lmList[23][1]+lmList[24][1])//2)
    except: pass
    try: centros["Joelho Esquerdo"] = (lmList[26][0], lmList[26][1])
    except: pass
    try: centros["Joelho Direito"] = (lmList[25][0], lmList[25][1])
    except: pass
    try: centros["Pe Direito"] = (lmList[28][0], lmList[28][1])
    except: pass
    try: centros["Pe Esquerdo"] = (lmList[27][0], lmList[27][1])
    except: pass
    return centros

def carregar_videos(parte):
    if parte in mapeamento_videos:
        vid1 = cv2.VideoCapture(mapeamento_videos[parte][0])
        vid2 = cv2.VideoCapture(mapeamento_videos[parte][1])
        return vid1, vid2
    return None, None

vid1 = vid2 = None
frame_count = 0

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = pose_detector.findPose(frame)
    lmList, _ = pose_detector.findPosition(frame, draw=False)

    display = background.copy()

    if lmList:
        centros = obter_pontos(lmList)

        try:
            pulso_direito = (lmList[19][0], lmList[19][1])
        except:
            pulso_direito = None

        nova_parte = None
        if pulso_direito:
            for parte, (x, y) in centros.items():
                if distancia(pulso_direito, (x, y)) < limite_distancia:
                    nova_parte = parte
                    break

        if nova_parte and nova_parte != parte_selecionada:
            parte_selecionada = nova_parte
            if vid1: vid1.release()
            if vid2: vid2.release()
            vid1, vid2 = carregar_videos(parte_selecionada)

        # Desenho dos pontos
        for parte, (x, y) in centros.items():
            cor = (0, 255, 0) if parte == parte_selecionada else (255, 0, 0)
            cv2.circle(frame, (x, y), 10, cor, cv2.FILLED)
            cv2.putText(frame, parte, (x - 40, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, cor, 2)

    # Mostra os vídeos se carregados
    if vid1 and vid2 and frame_count % 3 == 0:
        _, frame_vid1 = vid1.read()
        _, frame_vid2 = vid2.read()

        if frame_vid1 is not None and frame_vid2 is not None:
            frame_vid1 = cv2.resize(frame_vid1, (538, 593))
            frame_vid2 = cv2.resize(frame_vid2, (538, 593))
            display[255:255+593, 776:776+538] = frame_vid1  
            display[255:255+593, 166:166+538] = frame_vid2 

    # Webcam no canto (default 1920x1080)
    cam_preview = cv2.resize(frame, (315, 590))
    display[257:257+590, 1437:1437+315] = cam_preview

    # Título
    if parte_selecionada:
        texto = f"Selecionado: {parte_selecionada}"
        cv2.putText(display, texto, (1400, 900), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

    cv2.imshow("Mapeamento Musculo-Esqueletico", display)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
if vid1: vid1.release()
if vid2: vid2.release()
cv2.destroyAllWindows()