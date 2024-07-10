import figlet
import sys
import random


def main():
    idk = input("Input: ")
    convert(idk)


def convert(string):
    a = random.choice(figlet)
    print(a)
    print(figlet.a(string))


if __name__ == "__main__":
    main()
