def main():
  hello("world")
  goodbye("world")


def hello(name):
  print(f"hello, {name}")


def goodbye(name):
  print(f"goodbye, {name}")


if __name__ == "__main__":
  main()
#this part will run only when we run the program directly during checking
#it will not run when you import it as a module in other files as
__name__ == "the_filename" and hence it will not be "main"


pep8 : python enhancement proposal
tries to standardise the code that we write
