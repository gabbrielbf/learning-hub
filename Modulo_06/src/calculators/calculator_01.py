from typing import Dict
from flask import request as FlaskRequest

class Calculator1:
    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        splited_number = input_data / 3

        first_proccess_result = self.__first_proccess(splited_number)
        return first_proccess_result

    def __validate_body(self, body: Dict) -> float:
        if 'number' not in body:
            raise Exception('Body has a bad formatation!')

        input_data = body['number']
        return input_data

    def __first_proccess(self, first_number: float) -> float:
        first_step = (first_number / 4) + 7
        second_step = (first_step ** 2) * 0.257
        return second_step