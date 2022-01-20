#estoque.py

produto = input('Digite o nome do produto: ')
preco = float(input('Digite o preço: '))
quantidade = int(input('Digite a quantidade: '))
total = preco * quantidade

#informar produto, preço e quantidade
print('Nome do produto: ' , produto)
print('Preço do produto R$ ',  preco)
print('Quantidade: ', quantidade)
print('Total do estoque R$ %.2f ' % total)
