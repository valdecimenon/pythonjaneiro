class Produto:
    def __init__(self, id, descricao, preco, quantidade):
        self.__id = id
        self.__descricao = descricao
        self.preco = preco
        self.__quantidade = quantidade

    def __str__(self):
        return (f'Código: {self.id} \tDescrição: {self.descricao}  \tPreço Unitário: R$ {self.preco:.2f} \tQuantidade em Estoque: {self.quantidade}')

    @property
    def id(self):
        return self.__id

    @property
    def descricao(self):
        return self.__descricao

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidade(self):
        return self.__quantidade

    @id.setter
    def id(self, id):
        self.__id = id

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @quantidade.setter
    def quantidade(self, quantidade):
        self.quantidade = quantidade
