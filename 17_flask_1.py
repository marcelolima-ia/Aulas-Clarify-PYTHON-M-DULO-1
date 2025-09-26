import os
import sqlite3
from flask import Flask, redirect, url_for, request, render_template, session

# ====== CONFIG DO BANCO ======
# 1) BANCO NO DESKTOP (como no seu exemplo):
# DB_LOCAL = r"C:\Users\integral\Desktop\PythonByanca\meuBanco.db"

# 2) BANCO NA MESMA PASTA DO PROJETO (recomendado p/ testar):
DB_LOCAL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "meuBanco.db")

# ====== FUNÇÕES DO BANCO ======
def conectarBanco():
    conexao = sqlite3.connect(DB_LOCAL, check_same_thread=False)
    conexao.row_factory = sqlite3.Row
    return conexao

def criar_tabela():
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome  TEXT UNIQUE,
            senha TEXT
       )
    ''')
    conexao.commit()
    conexao.close()

def inserir_usuario(nome, senha):
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, senha)
        VALUES (?,?)
    ''', (nome, senha))
    conexao.commit()
    conexao.close()

def usuario_existe(nome):
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('SELECT 1 FROM usuarios WHERE nome = ?', (nome,))
    achou = cursor.fetchone() is not None
    conexao.close()
    return achou

def validar_login(nome, senha):
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('SELECT 1 FROM usuarios WHERE nome = ? AND senha = ?', (nome, senha))
    ok = cursor.fetchone() is not None
    conexao.close()
    return ok

def ver_usuarios_console():
    """Apenas para depuração no terminal."""
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('SELECT id, nome, senha FROM usuarios')
    for linha in cursor.fetchall():
        print(dict(linha))
    conexao.close()

def garantir_usuario_teste():
    """Se a tabela estiver vazia, cria um usuário padrão caio/123."""
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('SELECT COUNT(*) AS total FROM usuarios')
    total = cursor.fetchone()[0]
    conexao.close()
    if total == 0:
        try:
            inserir_usuario('caio', '123')
            print("Usuário de teste criado: caio / 123")
        except sqlite3.IntegrityError:
            pass

# ====== APP FLASK ======
app = Flask(__name__)
app.secret_key = "troque-esta-chave-em-producao"  # necessário para usar session

@app.route('/')
def pagina_inicial():
    user = session.get('user')
    return render_template('inicio.html', user=user)

@app.route('/entrar/')
def fazer_login():
    return render_template('login.html')

@app.route('/sair/')
def sair():
    session.pop('user', None)
    return redirect(url_for('pagina_inicial'))

@app.route('/pagina403/')
def pagina403():
    return render_template('pagina403.html')

@app.route('/welcome/')
def welcome():
    user = session.get('user')
    return render_template('welcome.html', user=user)

@app.route('/validador/', methods=['POST', 'GET'])
def validador():
    if request.method == 'POST':
        usuario = request.form.get('c_usuario', '').strip()
        senha = request.form.get('c_senha', '').strip()
    else:  # GET
        usuario = request.args.get('c_usuario', '').strip()
        senha = request.args.get('c_senha', '').strip()

    if validar_login(usuario, senha):
        session['user'] = usuario  # << guarda usuário logado
        return redirect(url_for('welcome'))
    else:
        return redirect(url_for('pagina403'))

# (Opcional) rota simples para cadastrar via URL/POST sem template próprio
# Ex.: POST para /cadastrar com form {"usuario": "novo", "senha": "1234"}
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    usuario = request.form.get('usuario', '').strip()
    senha = request.form.get('senha', '').strip()
    if not usuario or not senha:
        return "Informe usuario e senha", 400
    if usuario_existe(usuario):
        return "Usuário já existe", 409
    inserir_usuario(usuario, senha)
    return "Usuário cadastrado com sucesso", 201

@app.route('/registrar/', methods=['GET', 'POST'])
def registrar():
    if request.method == 'GET':
        # só mostra o formulário
        return render_template('registrar.html', erro=None)

    # POST: tenta criar usuário
    usuario = request.form.get('usuario', '').strip()
    senha = request.form.get('senha', '').strip()
    confirmar = request.form.get('confirmar', '').strip()

    if not usuario or not senha:
        return render_template('registrar.html', erro="Preencha usuário e senha.")
    if senha != confirmar:
        return render_template('registrar.html', erro="As senhas não conferem.")
    if usuario_existe(usuario):
        return render_template('registrar.html', erro="Usuário já existe. Tente outro.")

    inserir_usuario(usuario, senha)
    # depois de cadastrar, manda para o login
    return redirect(url_for('fazer_login'))

if __name__ == '__main__':
    criar_tabela()
    garantir_usuario_teste()
    # ver_usuarios_console()  # descomente para listar no terminal
    app.run('0.0.0.0', port=5000, debug=True)
