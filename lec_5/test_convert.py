import pytest
from convert import convert


def test_converion():
  assert convert(1) == 149597870700
  assert convert(50) == 7479893535000


def test_error():
  with pytest.raises(TypeError):
    convert("1") #an error will be raised if we give a string
    "a type error"
