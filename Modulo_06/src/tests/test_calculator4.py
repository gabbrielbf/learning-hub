from src.calculators.calculator4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler
from typing import Dict, List
from pytest import raises

class MockRequest:

    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler:

    def mean(self, numbers: List[float]) -> float:
        return 25

def test_calculate_integration():

    mock_request = MockRequest({
        'numbers': [10, 20, 30, 40]
    })

    calc4 = Calculator4(NumpyHandler())
    response = calc4.calculate(mock_request)

    assert response == {
        'data': {
            'Calculator': 4,
            'value': 25,
            'success': True
        }
    }