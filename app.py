from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurações de conexão com o banco de dados PostgreSQL
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@postgres.cuebxlhckhcy.us-east-1.rds.amazonaws.com:5432/postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgresaula:PostgresAula123!@postgres-aula.cuebxlhckhcy.us-east-1.rds.amazonaws.com:5432/postgresaula'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando o ORM SQLAlchemy
db = SQLAlchemy(app)

# Definindo a tabela 'teste' com o campo 'item'
class Tabela(db.Model):
    # __tablename__ = 'aluno_40'
    # id = db.Column(db.Integer, primary_key=True)
    # Nome = db.Column(db.String(200), nullable=False)
    # Telefone = db.Column(db.String(200), nullable=False)
    # Email = db.Column(db.String(200), nullable=False)
    # Nomepet= db.Column(db.String(200), nullable=False)

    # def __init__(self, item):
    #     self.item = item

    __tablename__ = 'aluno_40'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    nomepet = db.Column(db.String(200), nullable=False)

    def __init__(self, nome, telefone, email, nomepet):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.nomepet = nomepet


@app.route('/')
def index():
    db.create_all()
    return render_template('index.html')

# Rota para exibir o formulário e inserir dados
@app.route('/contato')
def contato():
    # Criando as tabelas na primeira execução
    #db.create_all()
    
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        # Capturar as informações do formulário
        nome = request.form.get('nome')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        nomepet= request.form.get('nomepet')
        
        # Criar um novo contato no banco
        novo_contato = Tabela(
        nome=nome,
        telefone=telefone,
        email=email,
        nomepet=nomepet
        )

        # Salva as informações no banco
        db.session.add(novo_contato)
        db.session.commit()
        return redirect(url_for('contato'))
    
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)

