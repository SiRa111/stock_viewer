from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

def main():
    if len(sys.argv) == 1:
        string = input("Input: ")
        f = random.choice(figlet.getFonts())
        figlet.setFont(font=f)
        print(f)
        a = figlet.renderText(string)
        print(a)
        return True

    elif len(sys.argv) == 3:
        valid_font = figlet.getFonts()
        if sys.argv[1] == "-f" or "-font":
            if sys.argv[2] in valid_font:
                string = input("Input: ")
                figlet.setFont(font=sys.argv[2])
                a = figlet.renderText(string)
                print(a)
            else:
                print("Invalid usage")
                sys.exit
        else:
            print("Invalid usage")
            sys.exit
    else:
        print("Invalid usage")
        sys.exit

if __name__ == "__main__":
    main()
