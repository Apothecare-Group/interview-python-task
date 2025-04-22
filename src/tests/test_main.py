def test_get_even_numbers():
    from src.main import get_even_numbers

    # Test with a standard list of integers
    assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    
    # Test with an empty list
    assert get_even_numbers([]) == []
    
    # Test with a list containing only odd numbers
    assert get_even_numbers([1, 3, 5]) == []
    
    # Test with a list containing only even numbers
    assert get_even_numbers([2, 4, 6]) == [2, 4, 6]
    
    # Test with negative numbers
    assert get_even_numbers([-1, -2, -3, -4]) == [-2, -4]
    
    # Test with a mixed list
    assert get_even_numbers([-1, 0, 1, 2, 3, 4]) == [0, 2, 4]