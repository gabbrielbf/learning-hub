from flask import Flask
from models.user import User
from database import db
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # <- Caminho que o SQLAlquemy vai utilizar para conectar-se com nosso banco

login_manager = LoginManager()
db.init_app(app) # Armazenando uma instância da classe SQLalchemy com o APP sendo o ponto de partida
login_manager.init_app(app)

if __name__ == '__main__':
    app.run()