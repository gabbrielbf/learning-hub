from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator4 import Calculator4

def calculator4_factory():
    numpy_handler = NumpyHandler()
    calc = Calculator4(numpy_handler)
    return calc