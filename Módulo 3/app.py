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
def get_tasks():

    task_list = []

    for task in tasks:
        task_list.append(task.dict()) # Lembre-se que a lista de tasks original lá em cima possui objetos instânciados da classe 'Task'.
                                      # Portanto todos eles possuem o método de retornar um dicionário com as informações que solicitamos
    output = {
                'tasks': task_list, # A variavel output guarda um dicionario com uma lista de tasks também em formato de dicionário
                'total_tasks': len(task_list) # <- Conta quantas tasks temos em nosso dicionário
            }
    return jsonify(output)

# Rota responsável por retornar APENAS uma única task
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):

    # Para cada tarefa na lista de tarefas faça isso
    for t in tasks:
        if t.id == id: # Se a tarefa da vez tiver um ID parecido com o ID parâmetrado
            return jsonify(t.dict()) # <- Retorne o dicionário específico

    # Se não, retorne uma mensagem de erro com o código do erro, no caso [404].
    return jsonify({'message': 'The ID could not be found'}), 404

if __name__ == '__main__':
    app.run(debug=True)