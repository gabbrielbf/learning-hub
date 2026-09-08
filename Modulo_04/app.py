from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.config['SQLALCHEMY_DATABASE-URI'] = 'sqlite:///database.db' # <- Caminho que o SQLAlquemy vai utilizar para conectar-se com nosso banco

db = SQLAlchemy(app) # Armazenando uma instância da classe SQLalchemy com o APP sendo o ponto de partida

