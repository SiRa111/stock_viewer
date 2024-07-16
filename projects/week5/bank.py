g = input("Greeting : ")
g1 = g.strip()
unwanted = ["hello","Hello","HELLO"]
unwanted1 =["h","H"]


def main():
    print(value(g1))


def value(greeting):
  for i in unwanted:
      if greeting.find(i) is int():
        return 0
  for _ in unwanted1:
      if greeting.find(_) is int() :
         return 20
      return 100


if __name__ == "__main__":
    main()
