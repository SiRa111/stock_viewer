import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search('([1-12]):([0-5]/d)?\s(am|AM|pm|PM)\sto\s([1-12]):([0-5]/d)?\s(?:am|AM|pm|PM)'):
        if match.group(3) == ('am'|'AM'):
            print(f"{match.group(1)}:{match.group(2) to {match.group(4)+12}:{match.group(5)}}")
        else:
            print(f"{match.group(1)+12}:{match.group(2) to {match.group(4)}:{match.group(5)}}")
    else:
        raise ValueError("ValueError")


if __name__ == "__main__":
    main()
