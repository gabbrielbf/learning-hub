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

        return jsonify({'message': 'User authenticated successfully'})

    return jsonify({'message': 'Inválid credentials'}), 400

if __name__ == '__main__':
    app.run()