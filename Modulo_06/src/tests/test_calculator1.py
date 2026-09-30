from src.calculators.calculator_01 import Calculator1
from typing import Dict
from pytest import raises

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

def test_calculate_body_no_formated():
    mock_request = MockRequest(body={ 'anything': 1 })
    calc1 = Calculator1()

    # Esse cara vai lançar um erro caso o "mock_request" acima esteja com o body
    # formatado incorretamente
    with raises(Exception) as excinfo:
        calc1.calculate(mock_request)

    assert str(excinfo.value) == 'Body has a bad formatation!'