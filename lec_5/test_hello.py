from hello import hello

def test_default():
  assert hello() == "hello, world"

def test_argument():
    assert hello("Simran") == "hello, Simran"

def test_list():#tests multiple values 
   for name in ["Hermionie", "Harry", "Ron"]:
      assert hello(name) == f"hello, {name}"
