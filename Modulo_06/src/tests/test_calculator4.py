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

