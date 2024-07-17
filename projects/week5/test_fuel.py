from fuel import convert, gauge
import pytest


def test_valid_fraction():
  assert convert("9/9") == 1
  with pytest.raises(ZeroDivisionError) : convert("8/0")
  with pytest.raises(ValueError) : convert("8/2")
  assert convert("8/9") == 89


def test_outputs():
  assert gauge(10) == "10%"
  assert gauge(78) == "78%"
  assert gauge(1) == "E"
  assert gauge(99) == "F"

