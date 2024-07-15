import hello

def test_default():
  assert hello.hello() == "hello, world"


def test_argument():
  assert hello.hello("xira") == "hello, xira"
