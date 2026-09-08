from app import db

class User(db.Model):
    # id[int], username[str], password[str]
    id = db.Column(db.Integer, primary_key=True) # Definindo o identificador com inteiro e criando a chave primária no qual serve como base
                                                 # para localizar determinado item dentro do banco
    pass