def main():
  name = input("What's your name ?: ")
  print(hello(name))


def hello(to="world"):
  #to is the default value
  return f"hello, {to}"a


if __name__ == "__main__":
  main()
