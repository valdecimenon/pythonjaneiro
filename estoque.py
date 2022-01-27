#Estoque.py

#cria lista vazia
produtos =      [ ]
quantidades = [ ]

def menu():
    opcao = -1
    
    while opcao != 0:
        print('############# Magazine da Maria ###########')
        print('#    Sistema de Controle de Estoque - versão 1.0 #')
        print('#    Desenvolvido por: Valdeci                               #')
        print('1 = Cadastrar')
        print('2 = Listar')
        print('3 = Apagar')
        print('0 = Sair')

        opcao = int(input('Qual opção? '))

        if opcao == 1:
            cadastrar()

        elif opcao == 2:
            listar()

        elif opcao == 3:
            apagar()

        elif opcao == 0:
            print('Saindo... Adeus!')

        else:
            print('Opção inválida')


def cadastrar():
    resp = 'S'

    while resp == 'S':
        
        nome = input('Digite o nome do produto: ')
        if nome in produtos:
            print('Produto já cadastrado!')
            continue

        #pede a quantidade e converte para inteiro
        quant = int(input('Digite a quantidade: '))

        #adiciona o produto na lista
        produtos.append(nome)

        #adiciona a quantidade na lista
        quantidades.append(quant)

        # 'S' ou 'N'
        resp = input('Quer continuar? (S)im ou (N)ão: ').upper() 


def listar():
        #mostra as listas
        print(produtos)
        print(quantidades)

def apagar():
    nome = input('Nome do produto para apagar do estoque: ')
    # CONTINUA AQUI NO PRÓXIMO CAPITULO

menu()




