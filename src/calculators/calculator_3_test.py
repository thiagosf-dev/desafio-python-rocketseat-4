from typing import Dict, List
from pytest import raises
from .calculator_3 import Calculator3
from ..drivers.numpy_handler import NumpyHandler
from ..drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandlerError:
    def variance(self, number: List[float]) -> float:
        return 1


class MockDriverHandler:
    def variance(self, number: List[float]) -> float:
        
        return 100


def test_calculate_with_variance_error():
    calculator3 = Calculator3(MockDriverHandlerError())
    with raises(Exception) as excinfo:
        calculator3.calculate(MockRequest({"numbers": [1, 2, 3, 4, 5]}))
    assert str(
        excinfo.value) == "Falha no processo: Variância menor que multiplicação."


def test_calculate():
    calculator3 = Calculator3(MockDriverHandler())
    response = calculator3.calculate(
        MockRequest({"numbers": [1, 1, 1, 1, 100]}))
    assert response == {
        'data': {
            'Calculator': 3,
            'value': 100,
            'Success': True
        }
    }
