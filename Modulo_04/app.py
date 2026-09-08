from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
db = SQLAlchemy(app) # Armazenando uma instância da classe SQLalchemy com o APP sendo o ponto de partida

