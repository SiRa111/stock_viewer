from bank import value

def test_hello():
  assert value("hello") == 0
  assert value("Hello, supp") == 0


def test_hstart():
  assert value("hi") == 20
  assert value("Hey") == 20


def test_greeting():
  assert value("good morning") == 100
  assert value("Guten morgen") == 100


def test_nums():
  assert value("123456") == 100
  assert value("12 34 56") == 100

def test_puncs():
  assert value("!whoa") == 100
  assert value("Intersting.") == 100
