import pytest
from unittest.mock import MagicMock, Mock
from safe_calculator import SafeCalculator

# PART 1 (without library)
class Authorizer:
    authorized = None

    def __init__(self, authorized):
        self.authorized = authorized

    def authorize(self):
        return self.authorized

def test_divide_should_not_raise_any_error_when_authorized_no_mock():
    safe_calculator = SafeCalculator(Authorizer(True))
    assert safe_calculator.add(1,1) == 2


def test_divide_should_not_raise_any_error_when_authorized_with_mock():
    thing = Mock("Authorizer")
    thing.authorize = MagicMock(return_value = True)
    safe_calculator = SafeCalculator(thing)
    assert safe_calculator.add(1,1) == 2
