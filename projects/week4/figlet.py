from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

def main():
    idk = input("Input: ")
    convert(idk)


def convert(string):
    a1 = random.choice(figlet.getFonts())
    #a = random.choice(a1)
    print(a1)



if __name__ == "__main__":
    main()
