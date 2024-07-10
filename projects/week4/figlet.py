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
        print(f)
        a = figlet.renderText(string)
        print(a)
        return True
    elif len(sys.argv) == 4:
        valid_font = figlet.getFonts()
        if sys.argv[2] == "-f" or "-font":
            if sys.argv[3] in valid_font:
                figlet.setFont(font=sys.argv[3])
                a = figlet.renderText(string)
                print(a)
            else:
                print("Invalid usage")
                sys.exit
        else:
            print("Invalid usage")
            sys.exit


if __name__ == "__main__":
    main()
