import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r'([1-12]):?([0-5]\d)?\s(am|AM|pm|PM)\sto\s([1-12]):?([0-5]\d)?\s(am|AM|pm|PM)', s):
        



if __name__ == "__main__":
    main()
