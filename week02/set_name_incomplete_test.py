import pytest
from thinking_sol import set_name

def test_firstName_char():
    assert set_name("Harold", "Adam", "Jobs") == True
    assert set_name("a" * 3, "a" * 4, "a" * 4) == True
    assert set_name("a" * 2, "a" * 4, "a" * 4) == False

def test_lastName_char():
    pass

def test_firstName_regex():
    assert set_name("Hello", "Adam", "Jobs") == True
    assert set_name("Hello-", "Adam", "Jobs") == True
    assert set_name("Hello-9", "Adam", "Jobs") == False
    assert set_name("Hel lo", "Adam", "Jobs") == False

def test_lastName_regex():
    assert set_name("Harold", "Adam", "Hello") == True
    assert set_name("Harold", "Adam", "Hello-") == True
    assert set_name("Harold", "Adam", "Hel lo") == True
    assert set_name("Harold", "Adam", "Hi 9") == False
