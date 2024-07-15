import pytest
from convert import convert


def test_converion():
  assert convert(1) == 149597870700
  assert convert(50) == 7479893535000


def test_error():
  with pytest.raises(TypeError):
    convert("1") #an error will be raised if we give a string
    "a type error"


def test_float_conversion():
  'assert convert(0.001) == 149597870.691'
  #this gives error due to the floating pt

  assert convert(0.001) == pytest.approx(149597870.691, abs=1e-5)
  #allows some float tolerance
