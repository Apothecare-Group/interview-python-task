from src.main import calculate_factorial
import pytest

def test_calculate_factorial():
    # Test factorial of 0
    assert calculate_factorial(0) == 1

    # Test factorial of 1
    assert calculate_factorial(1) == 1

    # Test factorial of a small positive number
    assert calculate_factorial(5) == 120

    # Test factorial of a larger positive number
    assert calculate_factorial(10) == 3628800

    # Test with invalid negative input
    with pytest.raises(ValueError):
        calculate_factorial(-1)

    # Test factorial of a boundary case
    assert calculate_factorial(2) == 2