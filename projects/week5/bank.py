g = input("Greeting : ")
g1 = g.strip()


def main():
    print(value(g1))


def value(greeting):
  if greeting.startswith("hello" or "Hello"):
      return 0
  elif greeting.startswith("h","H"):
      return 20
  else:
      return 100



if __name__ == "__main__":
    main()

