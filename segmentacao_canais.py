
#segmentacao_canais.py

import cv2

imagem = cv2.imread('frutas.jpg')
#devolve 3 canais
azul, verde, vermelho = cv2.split(imagem)

#exibe imagem em canais separados
cv2.imshow('Canal R', vermelho)
cv2.imshow('Canal G', verde)
cv2.imshow('Canal B', azul)


#salva imagem dos canais
cv2.imwrite('frutas_canal_r.jpg', vermelho)
cv2.imwrite('frutas_canal_g.jpg', verde)
cv2.imwrite('frutas_canal_b.jpg', azul)

cv2.waitKey(0)
cv2.destroyAllWindows()
