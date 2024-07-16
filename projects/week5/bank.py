g = input("Greeting : ")
g1 = g.strip()
unwanted = ["hello","Hello","HELLO"]
unwanted1 =["h","H"]


def main():
    print(value(g1))


def value(greeting):
  l=[]
  for i in greeting:
      l.append(i)
  print(l)

  if greeting in unwanted:
      return 0
  elif greeting.startswith("H""h"):
      return 20
  else:
      return 100


if __name__ == "__main__":
    main()
