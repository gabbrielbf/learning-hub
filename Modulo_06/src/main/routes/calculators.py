from flask import Blueprint, jsonify, request
from src.calculators.calculator1 import Calculator1
from src.main.factories.calculator2_factory import calculator2_factory

calc_route_bp = Blueprint('calc_routes', __name__)

@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculator1():
    calc = Calculator1()
    response = calc.calculate(request) # <- Recebendo a requisição do postman
    return jsonify(response)

@calc_route_bp.route('/calculator/2', methods=['POST'])
def calculator2():
    calc = calculator2_factory()
    response = calc.calculate(request) # <- Recebendo a requisição do postman
    return jsonify(response)