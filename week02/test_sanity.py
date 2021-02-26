'''
Basic function to show pytest functionality
'''
import pytest

def sum(x, y):
    return x + y

def test_sum():
    assert sum(1, 2) == 3

def test_failure():
    with pytest.raises(AssertionError):
        assert sum(1, 2) == 4
