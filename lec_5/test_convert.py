import pytest
from convert import convert


def test_converion():
  assert convert(1) == 149597870700
  assert convert(50) == 7479893535000
