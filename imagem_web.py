
#imagem_web.py

#pip install scikit-image
#pip install pafy
#pip install --upgrade youtube_dl

import cv2
from skimage import io
import pafy

#mostra imagem da web
def mostraWeb():
    imagem = io.imread('https://meupet.elanco.com/sites/g/files/adhwdz661/files/styles/paragraph_image/public/2020-04/bpc-48_-_filhotes.jpg?itok=A-H2qFJ7')
    cv2.imshow('Imagem web', imagem)


def exibeQuadro():
    captura = cv2.VideoCapture('video.mp4')
    ret, frame = captura.read()
    cv2.imshow('Exibindo um quadro do video', frame)

def exibeVideo():
    #use parâmetro (0) para capturar da webcam
    #captura = cv2.VideoCapture(0)
    captura = cv2.VideoCapture('video.mp4')

    while True:
        ret, frame = captura.read()
        cv2.imshow('Exibindo um quadro do video', frame)

        #aguarda 25 milissegundos
        if cv2.waitKey(25) & 0xFF == ord('s'):
            break

    captura.release()
    cv2.destroyAllWindows()


def exibeYoutube():
    url = 'https://www.youtube.com/watch?v=QcpahQr--7A'
    video = pafy.new(url)
    best = video.getbest()
    captura = cv2.VideoCapture(best.url)

    while True:
        ret, frame = captura.read()
        cv2.imshow('Exibindo video do youtube', frame)
        cv2.waitKey(25)

#mostraWeb()
#exibeQuadro()
#exibeVideo()
exibeYoutube()
