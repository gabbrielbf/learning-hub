from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# CRUD -> Create, read, update, delete.

tasks = []
task_id_control = 1

# Rota responsável por postar ou "inserir" um dado dentro da API
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json() # <- Recupera o que o cliente enviou pra a gente
    # A nova task criada abaixo será derivada da nossa classe Task sua descrição tem dois elementos no data.get pois queremos que
    # seu valor padrão seja vazio
    new_task = Task(id=task_id_control, title=data['title'], description=data.get('description', ''))
    task_id_control += 1 # lógica para definir que os IDs não se repitam, pois cada um deve ser unico
    tasks.append(new_task)
    return jsonify({'message': 'New task created sucessful'})

if __name__ == '__main__':
    app.run(debug=True)