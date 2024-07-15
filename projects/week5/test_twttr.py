from twttr import shorten
import pytest

def test_lower():
  assert shorten("short word") == "shrt wrd"

def test_upper():
  assert shorten("UPPERCASE HUH") == "PPRCS HH"

def test_num():
  assert shorten("1234") == "1234"

def test_nums():
  with pytest.raises(TypeError):
    shorten(1234)



