import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r'([1-12]):?([0-5]\d)?\s(am|AM|pm|PM)\sto\s([1-12]):?([0-5]\d)?\s(?:am|AM|pm|PM)', s):
        hr1 = match.group(1)
        min1 = match.group(2)
        more = match.group(3)
        hr2 = match.group(4)
        min2 = match.group(5)
        if more.lower() == 'am' and hr1 != 12 and min1 != None:
            print(f"{match.group(1)}:{match.group(2)} to {int(match.group(4))}:{match.group(5)}")
        elif more.lower() == 'am' and hr1 != 12 and min1 == None:
            print(f"{match.group(1)}:00 to {int(match.group(4))}:00")
        else:
            print(f"{int(match.group(1))}:{match.group(2)} to {match.group(4)}:{match.group(5)}")
    else:
        raise ValueError("ValueError")


if __name__ == "__main__":
    main()
