from database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # id[int], username[str], password[str], role[text]
    id = db.Column(db.Integer, primary_key=True) # Definindo o identificador com inteiro e criando a chave primária no qual serve como base
                                                 # para localizar determinado item dentro do banco
    username = db.Column(db.String(80), nullable=False, unique=True) # Definindo o limite de caracteres em 80, 'nullable' define se
                                                                      # se conseguimos criar um usuário com espaço vazio ou não
                                                                      # e 'unique' nos permite criar APENAS um usuário com o mesmo nome
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable =False, default='user') # <- Criado para ser usado em comparação nas requisições do app e assim
                                                                     # delimitar o que o usuário pode ou não fazer de acordo a sua permissão
    