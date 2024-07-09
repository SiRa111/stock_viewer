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

style guide : varies from company to company
you will develop your own style guide over the yrs



#------------GUIDELINES_TO_STYLE_CODE------------------
1.indentation
2.tab or spaces
3.maximum line length
4.blank lines (bw diff blocks of code)
5.imports

pylint - linter
checks for mistakes or maybe inconsistency in the code as per a style guide
pylint is very strict and you will get overwhelmed with how many errors you get in the styling of the code even though it works perfectly

___alternate__ : pycodestyle
reforms the entire code as per the standard for you :)

more popular : black
Henry Ford : "The customer may get any colour paint as long as its black :)
syntax: (in terminal)
black file_name.py

