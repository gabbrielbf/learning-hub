from flask import request as FlaskRequest
from typing import Dict, List

class Calculator2:
    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)

    def __validate_body(self, body: Dict) -> List[float]:
        if 'numbers' not in body:
            raise Exception('Body has a bad formatation!')

        input_data = body['numbers']
        return input_data