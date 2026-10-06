from flask import request as FlaskRequest
from typing import Dict, List
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:
    
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

    def __validate_body(self, body: Dict) -> List[float]:
        if 'numbers' not in body:
            raise HttpUnprocessableEntityError('Body has a bad formatation!')

        input_data = body['numbers']

        if not isinstance((input_data, list) or len(input_data) == 0):
            raise HttpUnprocessableEntityError('Body has a bad formatation!')

        return input_data

    def calculate_average(self, numbers: List[float]) -> float:
        total = sum(numbers)
        average = total / len(numbers)

        return average