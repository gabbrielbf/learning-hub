from src.calculators.calculator_01 import Calculator1
from typing import Dict

class MockRequest:
    # Classe responsável por gerar uma requisição ilusória
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    # Criando uma requisição ficticia
    mock_request = MockRequest(body={ 'number': 1 })

    calc1 = Calculator1()

    response = calc1.calculate(mock_request)

    # Testando o formato da resposta
    assert 'data' in response 
    assert 'Calculator' in response['data']
    assert 'result' in response['data']

    # Testando assertividade do cálculo
    assert response['data']['result'] == 14.25
    assert response['data']['Calculator'] == 1