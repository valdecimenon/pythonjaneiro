#principal.py

from veiculos import *

def principal():
    veiculo = Veiculo('Marca', 'modelo', 'placa', 2020)

    carro = Carro('VW', 'Polo', 'ABC-1234', 2015)
    moto = Motocicleta('Honda', 'CG 160', 'MMM-1234', 2021, 600)

    veiculo.abastecer()
    print(veiculo)

    carro.abastecer()
    print(carro)

    moto.abastecer()
    print(f'Placa da moto: {moto.placa}')
    print(f'Cilindrada da moto {moto.cilindrada}')

    lista = [veiculo, carro, moto, 'banana', 123, 1.0]
    for item in lista:
        if (isinstance(item, Carro)):
            print('Temos um Carro na lista')
        elif (isinstance(item, Motocicleta)):
            print('Temos um Motocicleta na lista')
        elif (isinstance(item, Veiculo)):
            print('Temos um Veiculo na lista')
        elif (isinstance(item, int)):
            print('Temos um int na lista')
        elif (isinstance(item, str)):
            print('Temos um str na lista')
        else:
            print('Item desconhecido na lista')


if __name__ == '__main__':
    principal()

    
