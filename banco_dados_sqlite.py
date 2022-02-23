
#banco_dados_sqlite.py


import sqlite3

#cria conexao
conexao = sqlite3.connect('escola.db')

#cria um cursor
cursor = conexao.cursor()

def criarTabela():
    sql = 'CREATE TABLE if not exists aluno (' \
            'id integer primary key, ' \
            'nome varchar(100), ' \
            'email varchar(100), ' \
            'telefone varchar(14))'

    #cria a tabela
    cursor.execute(sql)


def inserirDados():
    #comando sql
    sql = 'INSERT INTO aluno VALUES (?, ?, ?, ?)'

    #dados
    recset = [
                    (1, 'João da Silva', 'joao@gmail.com', '(42) 98412-1234'),
                    (2, 'Maria Padilha', 'maria@hotmail.com', '(42) 99933-4444'),
                    (3, 'Luiz Carlos', 'luiz@ig.com.br', '(42) 98402-0030')
                 ]

    #insere os dados na tabela
    for rec in recset:
        cursor.execute(sql, rec)

    #confirma a transação
        conexao.commit()


def listarDados():
    #seleciona todos os registros da tabela aluno
    cursor.execute('select * from aluno')

    #recupera os resultados
    recset = cursor.fetchall()

    #mostra na tela
    for rec in recset:
        print('ID: %d \t Nome: %-15s \t E-mail: %-18s \t Telefone: %-20s' % rec)

    #fecha conexão com o banco
    conexao.close()

#programa principal
if (__name__ == '__main__'):
    #criarTabela()
    #inserirDados()
    listarDados()
