from src.calculators.calculator3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler
from typing import Dict
from pytest import raises

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate_with_variance_error():
    mock_request = MockRequest({ 'numbers': [1, 2, 3, 4, 5] })
    calc3 = Calculator3(NumpyHandler())

    with raises(Exception) as exinfo:     
        calc3.calculate(mock_request)

    assert str(exinfo.value) == 'Failure in the process: Variance is less than multiplication'

def test_calculate():
    # mock_request = MockRequest({ 'numbers': [1, 2, 3, 4, 5] })
    # calc3 = Calculator3(NumpyHandler())
    
    # response = calc3.calculate(mock_request)

    pass