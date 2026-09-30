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