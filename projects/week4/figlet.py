from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


def main():
    idk = input("Input: ")
    convert(idk)


def convert(string):
    if len(sys.argv) == 2:
        f = random.choice(figlet.getFonts())
        figlet.setFont(font=f)
        a = figlet.renderText(string)
        print(a)
    elif len(sys.argv) == 4:
        



if __name__ == "__main__":
    main()
