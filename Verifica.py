#verifica.py

#Algoritmo
#1. Cria uma lista de cores
#2. Pergunta ao usuário o nomde de uma cor
#3. Diz para o usuário se a cor existe na lista
#4. Se não está na lista, adiciona (anexar=append)
lista_cor = ['Azul','Amarelo','Vermelho','Verde','Branco','Preto','Lilás','Roxo','Violeta','Cinza','Dourado','Azul','Verde','Preto','Azul','Vermelho','Branco','Roxo','Lilás']
x = input('Digite uma cor: ')
if x in lista_cor:
    print('Está na lista')
else:
    print('Não está na lista')
    lista_cor.append(x)
