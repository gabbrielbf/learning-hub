from src.calculators.calculator3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler
from typing import Dict

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    calc3 = Calculator3(NumpyHandler())
    calc3.calculate()