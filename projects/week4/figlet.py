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
        return a

    elif len(sys.argv) == 3:
        valid_font = figlet.getFonts()
        if sys.argv[1] == "-f" or sys.argv[1] == "-font":
            if sys.argv[2] in valid_font:
                if len(sys.argv[1]) == 2 or len(sys.argv[1]) == 5:
                    string = input("Input: ")
                    figlet.setFont(font=sys.argv[2])
                    a = figlet.renderText(string)
                    return a
                else:
                    sys.exit
                    print("Invalid Usage")
                    return False

            else:
                sys.exit
                print("Invalid Usage")
                return False

        else:
            sys.exit
            print("Invalid Usage")
            return False

    else:
        sys.exit
        print("Invalid Usage")
        return False

a = main()
if a == False:
    print("Invalid Usage")
else:
    print(a)

