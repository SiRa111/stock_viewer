g = input("Greeting : ")
g1 = g.strip()
unwanted = ["hello","Hello","HELLO"]
unwanted1 =["h","H"]


def main():
    print(value(g1))


def value(greeting):
  if greeting.find("Hello"or"hello") is int():
      return 0
  elif greeting.find("h"or"H") is int() :
      return 20
  else:
      return 100


if __name__ == "__main__":
    main()
