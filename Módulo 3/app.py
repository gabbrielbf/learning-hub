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

# Rota responsável por atualizar uma task específica através do ID
@app.route('/tasks/<int:id>', methods=['PUT'])
def uptate_task(id):

    # Inciamos a task como vazia e conferimos ID por ID dentro das nossas tarefas cadastradas
    task = None
    for t in tasks:
        if t.id == id:
            task = t

    if task == None: # Caso nossa tarefa seja VAZIO ou 'None' retornamos um erro
        return jsonify({'message': 'The ID could not be found'}), 404

    # Se chegarmos aqui quer dizer que passamos por todas as conferências de erro
    data = request.get_json() # <- Recuperando os dados obtidos pelo usuário e abaixo atualizaremos
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    return jsonify({'message': 'Task update successfully'})

# Rota responsável pela deleção de uma task através do ID assim como o 'PUT'
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    pass
    
if __name__ == '__main__':
    app.run(debug=True)