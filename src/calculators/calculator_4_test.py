from typing import Dict, List
from pytest import raises
from .calculator_4 import Calculator4
from ..drivers.numpy_handler import NumpyHandler
from ..drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandlerError:
    def average(self, number: List[float]) -> float:
        return 1


class MockDriverHandler:
    def average(self, number: List[float]) -> float:
        return 9


def test_calculate_with_average_error():
    calculator4 = Calculator4(MockDriverHandlerError())
    with raises(Exception) as excinfo:
        calculator4.calculate(MockRequest({"number": [1, 2, 3, 4, 5]}))
    assert str(
        excinfo.value) == "body mal formatado!"


def test_calculate():
    calculator4 = Calculator4(MockDriverHandler())
    response = calculator4.calculate(
        MockRequest({"numbers": [10, 8, 10, 8]}))
    assert response == {
        'data': {
            'Calculator': 4,
            'value': 9,
            'Success': True
        }
    }


def test_calculate_integration():
    calculator4 = Calculator4(NumpyHandler())
    response = calculator4.calculate(
        MockRequest({"numbers": [10, 9, 8, 7]}))
    assert response == {
        'data': {
            'Calculator': 4,
            'value': 8.5,
            'Success': True
        }
    }
