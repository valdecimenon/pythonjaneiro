#veiculos.py

#classe mãe ou super classe
class Veiculo:

    #construtor ou inicializador
    def __init__ (self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

    def ligar(self):
        print('Veiculo ligado...')

    def abastecer(self):
        print('Veiculo abastecendo...')

    #funções builtin: funções prontas que inicia por __xxx__
    def __str__(self):
        return 'Placa do veículo: ' + self.placa

#classe filha
class Carro(Veiculo):
    def __init__  (self, marca, modelo, placa, ano):
        super().__init__ (marca, modelo, placa, ano)

    #sobrescreve a função da classe mãe
    def __str__(self):
        return 'Placa do carro: ' + self.placa

#classe filha
class Motocicleta(Veiculo):
    def __init__  (self, marca, modelo, placa, ano, cilindrada):
        super().__init__ (marca, modelo, placa, ano)
        self.cilindrada = cilindrada







