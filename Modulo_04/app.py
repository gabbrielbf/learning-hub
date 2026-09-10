from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, logout_user, login_required
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(  # <- Caminho que o SQLAlquemy vai utilizar para conectar-se com nosso banco
    os.path.dirname(__file__), # Usando o os.path para localizar o arquivo LITERAL do banco de dados
    'instance',
    'database.db'
)

login_manager = LoginManager()
db.init_app(app) # Armazenando uma instância da classe SQLalchemy com o APP sendo o ponto de partida
login_manager.init_app(app)

# Criando tabelas vazias no banco caso as mesmas não existam
with app.app_context():
    db.create_all()

# View login
login_manager.login_view = 'login' # <- Setando como 'login' para encontrar a rota de login na login abaixo

# Esse decorador abaixo nos permite recuperar com flask o objeto cadastrado dentro do banco de dados no formato da nossa classe 'User'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/login', methods=['POST'])
def login():

    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Lógica de login
    if username and password:

        # Váriavel abaixo está armazenando o primeiro usuário com o mesmo nome da variável username acima, o método "first()" trabalha
        # em conjunto com o parâmetro "unique" da classe User para garantir que temos APENAS um usuário com o mesmo nome
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:

            login_user(user) # <- Autenticando o usuário com função da biblioteca

            return jsonify({'message': 'User authenticated successfully'})

    return jsonify({'message': 'Invalid credentials'}), 400

@app.route('/logout', methods=['GET'])
@login_required
def logout():

    logout_user()
    return jsonify ({'message': 'Logout successful'})

@app.route('/user', methods=['POST'])
def create_user():

    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username and password:

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        return jsonify({'message': 'User registred successfully'})

    return jsonify({'message': 'Invalid credentials'}), 401

# Recuperando os dados de determinado usuário
@app.route('/user/<int:id_user>', methods=['GET'])
@login_required
def read_user(id_user):

    user = User.query.get(id_user)

    if user:
        return {'username': user.username}

    return jsonify({'message': 'User not found'}), 404

# Atualizando determinado usuário
@app.route('/user/<int:id_user>', methods=['PUT'])
@login_required
def update_user(id_user):

    user = User.query.get(id_user)

    if user:
        return jsonify({'message': f'User [{id_user}] successfully updated'})
    
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run()