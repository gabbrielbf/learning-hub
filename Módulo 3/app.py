from flask import Flask, request
from models.task import Task

app = Flask(__name__)

# CRUD -> Create, read, update, delete.

tasks = []

# Rota responsável por postar ou "inserir" um dado dentro da API
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json() # <- Recupera o que o cliente enviou pra a gente
    return 

if __name__ == '__main__':
    app.run(debug=True)