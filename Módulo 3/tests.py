# Arquivo designado a testes relacionados a nossa pequena API
import pytest, requests

# CRUD -> Create, read, update, delete.
# Testes abaixo se basearão letra a letra com uma URL fixa

BASE_URL = 'http://127.0.0.1:5000'
tasks = [] # <- Adicionando tarefas criadas para testarmos as demais atividades com os endpoints 'RUD'.

# Create
def test_create_task():

    new_task_data = {
        'title': 'New task',
        'description': 'Description of new task'
    }
    resposne = requests.post(f'{BASE_URL}/tasks', json=new_task_data)
    assert resposne.status_code == 200