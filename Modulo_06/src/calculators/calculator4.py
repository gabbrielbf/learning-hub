from flask import request as FlaskRequest
from typing import Dict, List
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator4:

    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        average = self.__calculate_average(input_data)
        formated_response = self.__formated_response(average)
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if 'numbers' not in body:
            raise HttpUnprocessableEntityError('Body has a bad formatation!')

        input_data = body['numbers']

        if not isinstance((input_data, list) or len(input_data) == 0):
            raise HttpUnprocessableEntityError('Body has a bad formatation!')

        return input_data

    def __calculate_average(self, numbers: List[float]) -> float:
        total = sum(numbers)
        average = total / len(numbers)

        return average

    def __formated_response(self, average: float) -> Dict:
        return{
            'data': {
                'Calculator': 4,
                'value': average,
                'success': True
            }
        }
