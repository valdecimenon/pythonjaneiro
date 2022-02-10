#arquivo_csv.py

#permite gravar e ler arquivos .csv do Excel

import csv

#Gravando um arquivo .csv
def gravar():
    tabela = (('PRODUTO', 'UNIDADE', 'PREÇO UNITÁRIO', 'QUANTIDADE ESTOQUE', 'VALOR TOTAL'),
                    ('Açúcar', '2 Kg',      3.59, 10, 35.90),
                    ('Biscoito', '200 Gr', 1.19, 10, 11.90)
                  )
    # cria um objeto de escrita
    saida = csv.writer(open('tabela.csv', 'w', newline=''), delimiter = ';')

    #escreve as tuplas no arquivo
    saida.writerows(tabela)

#Lendo arquivo .csv
def ler():
    tabela = csv.reader(open('tabela.csv'))

    #para cada linha do arquivo, imprima
    for lista in tabela:
        print(lista[0].split(';')[0])


if (__name__  == '__main__'):
    #gravar()
    ler()
