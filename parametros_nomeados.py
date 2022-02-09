#parametros_nomeados.py


def mensagem(tipo = 'Mensagem', msg = 'Bom dia'):
    print(f'{tipo}: {msg}')



mensagem(tipo='Alerta')
mensagem(msg='Boa tarde')
mensagem(msg='Boa noite', tipo='Alerta')

#end = parâmetro nomeado do  print
print(1, end=' ')
print(2,  end=' ')
print(3,  end=' ')
