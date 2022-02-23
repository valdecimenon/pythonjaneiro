
#banco_dados_mysql.py

#python -m pip install --upgrade pip

# cd scripts
#pip3 install PyMySQL

#criar banco escola.db usando sqlitestudio

import pymysql

def listaDatabases():
    #executa um comando SQL
    cursor.execute('show databases')

    #recupera o resultado
    recordset = cursor.fetchall()   #fetch = buscar

    #mostra o resultado
    for registro in recordset:
        print(record)



if (__name__ == '__main__'):
    #cria conexão com o banco
    conexao = pymysql.connect(db='mysql', user='root', passwd='softgraf')
    #cria um cursor
    cursor = conexao.cursor()
    listaDatabases()

