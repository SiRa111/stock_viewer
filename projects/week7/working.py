import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r'([1-12]):?([0-5]\d)?\s(am|AM|pm|PM)\sto\s([1-12]):?([0-5]\d)?\s(am|AM|pm|PM)', s):
        if match.group(3) == ('am' or 'AM'):
            


        else:
            ...
    else:
        raise ValueError("ValueError")




if __name__ == "__main__":
    main()
