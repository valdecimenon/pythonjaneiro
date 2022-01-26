#Login.py

#Algoritmo
#1. Criar uma lista com nomes de usuários, contendo vários usuários
#2. Perguntar o nome do usuário
#3. Verificar se o usuário está na lista
#4. Informar se o usuário existe ou nao

usuarios = ['Andre','Gerson','Marise','Thiago','Jose Roberto']
usuario = input('Usuário: ').title()

if usuario in usuarios:
    print('Usuário Válido')
else:
    print('Usuário Inválido')
