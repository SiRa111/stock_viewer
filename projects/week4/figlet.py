import pyfiglet
import sys
import random

fig() = pyfiglet.figlet_format()

def main():
    idk = input("Input: ")
    convert(idk)


def convert(string):
    a1 = random.choice(pyfiglet.figlet_format)
    #a = random.choice(a1)
    print(a1)



if __name__ == "__main__":
    main()
