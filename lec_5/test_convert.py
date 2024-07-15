import pytest
from convert import convert


def test_converion():
  assert convert(1) == 149597870700
