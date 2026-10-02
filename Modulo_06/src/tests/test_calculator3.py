from src.calculators.calculator3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler
from typing import Dict, List
from pytest import raises
# from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

# class MockDriverHandler(DriverHandlerInterface):

#     def standard_derivation(self, numbers: List[float]) -> float:
#         return 5

def test_calculate_with_variance_error():
    mock_request = MockRequest({ 'numbers': [1, 2, 3, 4, 5] })
    calc3 = Calculator3(NumpyHandler())

    with raises(Exception) as exinfo:     
        calc3.calculate(mock_request)

    assert str(exinfo.value) == 'Failure in the process: Variance is less than multiplication'

def test_calculate():
    mock_request = MockRequest({ 'numbers': [1, 1, 1, 1, 100] })
    calc3 = Calculator3(NumpyHandler())
    
    response = calc3.calculate(mock_request)

    assert response == {'data': {'Calculator': 3, 'value': 1568.16, 'Success': True}}