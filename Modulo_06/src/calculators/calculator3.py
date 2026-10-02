from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator3:

    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)



    def __validate_body(self, body: Dict) -> List[float]:
        if 'numbers' not in body:
            raise Exception('Body has a bad formatation!')

        input_data = body['numbers']
        return input_data

    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers)
        return variance