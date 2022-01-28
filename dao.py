from produto import Produto

SQL_SALVA_PRODUTO = 'INSERT into produto (descricao, preco, quantidade) values (%s, %f, %d)'
SQL_LISTA_PRODUTOS = 'SELECT id, descricao, preco, quantidade FROM produto'
SQL_PRODUTO_POR_ID = 'SELECT id, descricao, preco, quantidade FROM produto WHERE id = %d'
SQL_DELETA_PRODUTO = 'DELETE FROM produto WHERE id = %d'
SQL_ATUALIZA_PRODUTO = 'UPDATE produto SET descricao=%s, preco=%f, quantidade=%d where id = %d'

class ProdutoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, produto):
        cursor = self.__db.connection.cursor()

        if (produto.id):
            cursor.execute(SQL_ATUALIZA_PRODUTO, (produto.descricao, produto.preco, produto.quantidade, produto.id))
        else:
            cursor.execute(SQL_SALVA_PRODUTO, (produto.descricao, produto.preco, produto.quantidade))
            produto.id = cursor.lastrowid

        self.__db.connection.commit()
        return produto

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_LISTA_PRODUTOS)
        produtos = traduz_produtos(cursor.fetchall())
        return produtos

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_PRODUTO_POR_ID, (id))
        tupla = cursor.fetchone()
        return Produto(tupla[0], tupla[1], tupla[2], tupla[3])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_PRODUTO, (id))
        self.__db.connection.commit()


def traduz_produtos(produtos):
    def cria_produto_com_tupla(tupla):
        return Produto(tupla[0], tupla[1], tupla[2], tupla[3])
    return list(map(cria_produto_com_tupla, produtos))