def main():
  name = input("What's your name ?: ")
  hello(name)


def hello(to="world"):
  #to is the default value
  print("hello,", to)


if __name__ == "__main__":
  main()
