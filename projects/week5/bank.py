g = input("Greeting : ")
g1 = g.strip()
unwanted = ["hello","Hello","HELLO"]
unwanted1 =["h","H"]


def main():
    print(value(g1))


def value(greeting):
  if greeting[0:5] in unwanted:
     return 0
  elif greeting[0] in unwanted1:
     return 20
  else:
     return 100


if __name__ == "__main__":
    main()
