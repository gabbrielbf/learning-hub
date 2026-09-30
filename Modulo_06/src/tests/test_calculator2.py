from src.calculators.calculator2 import Calculator2
from typing import Dict

class MockRequest:
    # Classe responsável por gerar uma requisição ilusória
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={ 'numbers': [2, 3, 4, 5.4] })
    calc2 = Calculator2()
    calc2.calculate(mock_request)