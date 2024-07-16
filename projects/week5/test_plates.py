from plates import is_valid

def test_alpha():
  assert is_valid("q") == "Invalid"
  assert is_valid("QWERTYU") == "Invalid"
  assert is_valid("")
