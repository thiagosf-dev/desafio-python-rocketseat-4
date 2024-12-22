from flask import Blueprint, request, jsonify
from ..factories.calculator1_factory import calculator1_factory
from ..factories.calculator2_factory import calculator2_factory
from ..factories.calculator3_factory import calculator3_factory
from ..factories.calculator4_factory import calculator4_factory
from ...errors.error_controller import handle_error

calc_route_bp = Blueprint('calc_route', __name__)


@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculator_1():
    try:
        calc = calculator1_factory()
        response = calc.calculate(request)
        return jsonify(response), 200
    except Exception as e:
        error_response = handle_error(e)
        return jsonify(error_response), error_response["status_code"]


@calc_route_bp.route('/calculator/2', methods=['POST'])
def calculator_2():
    try:
        calc = calculator2_factory()
        response = calc.calculate(request)
        return jsonify(response), 200
    except Exception as e:
        error_response = handle_error(e)
        return jsonify(error_response), error_response["status_code"]


@calc_route_bp.route('/calculator/3', methods=['POST'])
def calculator_3():
    try:
        calc = calculator3_factory()
        response = calc.calculate(request)
        return jsonify(response), 200
    except Exception as e:
        error_response = handle_error(e)
        return jsonify(error_response), error_response["status_code"]

@calc_route_bp.route('/calculator/4', methods=['POST'])
def calculator_4():
    try:
        calc = calculator4_factory()
        response = calc.calculate(request)
        return jsonify(response), 200
    except Exception as e:
        error_response = handle_error(e)
        return jsonify(error_response), error_response["status_code"]
