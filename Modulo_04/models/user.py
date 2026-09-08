from app import db

class User(db.Model):
    # id[int], username[str], password[str]
    id = db.Column(db.Integer, primary_key=True) # Definindo o identificador com inteiro e criando a chave primária no qual serve como base
                                                 # para localizar determinado item dentro do banco
    user_name = db.Column(db.String(80), nullable=False, unique=True) # Definindo o limite de caracteres em 80, 'nullable' define se
                                                                      # se conseguimos criar um usuário com espaço vazio ou não
                                                                      # e 'unique' nos permite criar APENAS um usuário com o mesmo nome
    password = db.Column(db.String(80), nullable=False)
    pass