import pytest
from myapp.calculator import add, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(6, 7) == 42


def test_divide():
    assert divide(8, 2) == 4.0


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot Divide by Zero"):
        divide(8, 0)
