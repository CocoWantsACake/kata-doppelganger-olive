import pytest

from safe_calculator import SafeCalculator

# PART 1 (without library)
class Authorizer:
    authorized = None

    def __init__(self, authorized):
        self.authorized = authorized

    def authorize(self):
        return self.authorized

def test_divide_should_not_raise_any_error_when_authorized():
    safe_calculator = SafeCalculator(Authorizer(True))
    assert safe_calculator.add(1,1) == 2
