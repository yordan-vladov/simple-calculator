# tests/test_calculator.py
from simple_calculator.calculator import add, subtract

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(5, 3) == 2

def test_add_floats():
    assert add(0.1,0.2) == 0.3
