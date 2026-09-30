from typing import Dict
from flask import request as FlaskRequest

class Calculator1:
    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        splited_number = input_data / 3

        first_proccess_result = self.__first_proccess(splited_number)
        second_proccess_result = self.__second_proccess(splited_number)

        calc_result = first_proccess_result + second_proccess_result + splited_number
        response = self.format_response(calc_result)
        return response

    def __validate_body(self, body: Dict) -> float:
        if 'number' not in body:
            raise Exception('Body has a bad formatation!')

        input_data = body['number']
        return input_data

    def __first_proccess(self, first_number: float) -> float:
        first_step = (first_number / 4) + 7
        second_step = (first_step ** 2) * 0.257
        return second_step

    def __second_proccess(self, second_number: float) -> float:
        first_step = (second_number ** 2.121)
        second_step = (first_step / 5) + 1
        return second_step

    def format_response(self, calc_result: float) -> Dict:
        return {
            "data":{
                "Calculator": 1,
                "Result": round(calc_result, 2)
            }
        }
