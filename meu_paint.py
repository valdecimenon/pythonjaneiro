#meu_paint.py

#Biblioteca opencv = computação visual
import cv2

def eventoClique(evento, x, y, flags, param):
    if evento == cv2.EVENT_LBUTTONDOWN:
        #print(x, ', ', y)
        pt = [x, y]
        #altera a cor do pixel
        img = cv2.circle(imagem, pt, 20, cor, -1)
        cv2.imshow('Meu Photoshop', img)


#branco r,g,b
cor = [255, 255, 255]

imagem = cv2.imread('frutas.jpg')
cv2.imshow('Meu Photoshop', imagem)


cv2.setMouseCallback('Meu Photoshop', eventoClique)


cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('D:/Curso Pyton Noite/Aula07/frutas_paint.jpg', imagem)
