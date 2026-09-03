from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# CRUD -> Create, read, update, delete.

tasks = []
task_id_control = 1

# Rota responsável por postar ou "inserir" um dado dentro da API
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json() # <- Recupera o que o cliente enviou pra a gente

    # A nova task criada abaixo será derivada da nossa classe Task. Sua descrição tem dois elementos no data.get pois queremos que
    # seu valor padrão seja vazio
    new_task = Task(id=task_id_control, title=data['title'], description=data.get('description', ''))
    task_id_control += 1 # lógica para definir que os IDs não se repitam, pois cada um deve ser unico
    tasks.append(new_task)
    return jsonify({'message': 'New task created successfull'})

# Rota responsável por retornar um dicionário com os dados de cada task
@app.route('/tasks', methods=['GET'])
def get_task():
    
    output = {
                'tasks': [ # A variavel output retorna um dicionario com uma chave que possui como valor uma lista possuindo
                           # as inforamções da nossa classe Task. Possui também um contador de quantas tasks tem em nosso dicionário
                    {
                    'id': 0, 
                    'title': 'str', 
                    'description': 'str', 
                    'completed': True
                    }
                ], 
                'total_tasks': 0
            }

if __name__ == '__main__':
    app.run(debug=True)