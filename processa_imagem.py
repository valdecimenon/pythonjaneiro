
#processa_imagem.py

import cv2

imagem = cv2.imread('frutas.jpg')
print('Resulação: ', imagem.shape)
print('Total de pixels: ', imagem.size)  #675x1200x3

#obtém a cor de um único pixel
valorPixel = imagem[150,150]
print('Intensidade RGB: ', valorPixel)

#converte para cinza o obtém a cor
cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
valorPixel = cinza[150,150]
print('Cinza: ', valorPixel)

#altera a cor de um único pixel
imagem[140,20] = [255,255,255]

#altera a cor da linha 150 na imagem, criando um traço branco
for coluna in range(0,1200):
    imagem[150,coluna] = [255,255,255]


cv2.imshow('Pixel alteraldo', imagem)
