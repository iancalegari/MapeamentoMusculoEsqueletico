import cv2
import cvzone       
import numpy as np

# Background
background = cv2.imread('background.png')
background = cv2.resize(background, (1920, 1080)) # ajustar de acordo com o fundo usado background é 1920x1080 e background2 é 1280x720

vid = cv2.VideoCapture('videos/membroinf3Esq.mp4')
vid2 = cv2.VideoCapture('videos/membroinf3Musc.mp4')
cap = cv2.VideoCapture(0)

# Contador controle velocidade
frame_count = 0

while True:
    # Pular 1 frame pra ficar 1.5x 
    if frame_count % 3 == 0:
        vid.read()   
        vid2.read()  

    success, frame = vid.read()
    success1, frame1 = vid2.read()
    success2, frame2 = cap.read()
    
    if not success or not success1 or not success2:
        break

    display = background.copy()

    #configurado pro background2 com 1280 x 720    
    
    #frame = cv2.resize(frame, (359, 395))
    #frame1 = cv2.resize(frame1, (359, 395))
    #frame2 = cv2.resize(frame2, (405, 210))  

    #display[170:170+395, 439:439+359] = frame    # Vídeo 1 (cabecaEsq)
    #display[170:170+395, 33:33+359] = frame1      # Vídeo 2 (cabecaMusc) 
    #display[286:286+210, 843:843+405] = frame2  # Webcam 

    #configurado pro background com 1920 x 1080  

    frame = cv2.resize(frame, (538, 593))
    frame1 = cv2.resize(frame1, (538, 593))
    frame2 = cv2.resize(frame2, (608, 315))  

    display[255:255+593, 659:659+538] = frame      # Vídeo 1 (cabecaEsq)
    display[255:255+593, 49:49+538] = frame1       # Vídeo 2 (cabecaMusc) 
    display[429:429+315, 1264:1264+608] = frame2   # Webcam

    cv2.imshow("Mapeamento Musculo-Esqueletico", display)

    # ajustar FPS atualmente 30
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

    frame_count += 1

cap.release()
cv2.destroyAllWindows()
