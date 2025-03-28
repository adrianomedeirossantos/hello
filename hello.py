def say_hello():
    return "Hello, world!"

# test_hello.py
import pytest
from hello import say_hello

def test_say_hello():
    assert say_hello() == "Hello, world!"
