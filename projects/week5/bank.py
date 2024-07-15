g = input("Greeting : ")
g1 = g.strip()
unwanted = "helloHelloHELLO"
unwanted1 = "hH"

def main():
    print(value(g1))


def value(greeting):
  if greeting in unwanted:
      return 0
  elif greeting in unwanted1:
      return 20
  else:
      return 100



if __name__ == "__main__":
    main()

