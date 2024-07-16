from plates import is_valid

def test_alpha():
  assert is_valid("q") == "Invalid"
  assert is_valid("QWERTYU") == "Invalid"


def test_first_two():
  assert is_valid("54gh") == "Invalid"
  assert is_valid("jk") == "Valid)
  assert is_valid("jkl90") == "Valid"


def test_only_alnum():
  assert is_valid("gh_ij") == "Invalid"
  assert is_valid("whoa:90") == "Invalid"
  assert is_valid("welp./87") == "Invalid"
  assert is_valid("ghji980") == "Valid"

def first_non_zero():
  assert is_valid("gh009") == "Invalid"
  assert is_valid("gh909") == "Valid"

def end_num():
  assert is_valid("gh09ji") == "Invalid"
  assert is_valid("ghji90") == "Valid"
