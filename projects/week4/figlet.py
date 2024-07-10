import pyfiglet
import sys
import random


def main():
    idk = input("Input: ")
    convert(idk)


def convert(string):
    a1 = pyfiglet.figlet_format(string)
    #a = random.choice(a1)
    print(a1)



if __name__ == "__main__":
    main()
