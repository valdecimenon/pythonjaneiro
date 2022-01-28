from produto import Produto
#Terminal: pip3 install flask==0.12.2
from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'softgraf'

p1 = Produto(1, 'TV LED 40', 1900.99, 20)
p2 = Produto(2, 'COMPUTADOR I5', 5.900, 10)
p3 = Produto(3, 'Mouse', 29.90, 50)
lista = [p1, p2, p3]

@app.route('/')
def index():
    #return '<h1>Olá Flask!</h1>'
    return render_template('relatorio.html', titulo='Relatório de estoque', produtos=lista)

@app.route('/cadastrar')
def cadastrar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    return render_template('cadastro.html', titulo='Cadastro de Produtos')

@app.route('/salvar', methods=['POST'])
def salvar():
    id = request.form['id']
    descricao = request.form['descricao']
    preco = request.form['preco']
    quantidade = request.form['quantidade']
    produto = Produto(id, descricao, preco, quantidade)
    lista.append(produto)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['senha'] == '123':
            session['usuario_logado'] = request.form['usuario']
            flash(request.form['usuario'] + ' logou com sucesso!')
            return redirect(url_for('index'))
    else:
        flash('Senha inválida! Tente novamente')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado')
    return redirect(url_for('index'))

app.run(debug=True)
#app.run(debug=True, host='127.0.0.1', port=80)