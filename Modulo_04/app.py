from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # <- Caminho que o SQLAlquemy vai utilizar para conectar-se com nosso banco

login_manager = LoginManager()
db.init_app(app) # Armazenando uma instância da classe SQLalchemy com o APP sendo o ponto de partida
login_manager.init_app(app)

# View login
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

            return jsonify({'message': 'User authenticated successfully'})

    return jsonify({'message': 'Invalid credentials'}), 400

if __name__ == '__main__':
    app.run()