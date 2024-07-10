import figlet
import sys
import random

def main():
  idk = input("Input: ")
  convert(idk)

def convert(string):
  if len(sys.argv) == 2:
    a = random.choice(figlet)
    return figlet.a



if __name__ == "__main__":
  main()
