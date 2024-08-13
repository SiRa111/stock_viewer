
from numb3rs import validate

def test_four_num():
  assert validate("0") == False
  assert validate("0.0.0.") == False
  assert validate("255.255.255") == False

def test_valid_nums():
  assert validate("276.0.0.1") == False
  assert validate("3000.5.6.7") == False
  assert validate("567.890.1000.5783945") == False
  assert validate("1.2.3.4.5") == False

def test_no_extra_chars():
  assert validate("0.0.0.0.") == False
  assert validate("0..0.0.0") == False

def test_only_nums():
  assert validate("cat") == False
  assert validate("dog") == False


