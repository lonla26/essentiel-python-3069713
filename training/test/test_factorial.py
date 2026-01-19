import pytest
from factorial import factorial

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 10
    assert factorial(3) == 6  