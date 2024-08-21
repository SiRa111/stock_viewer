import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r'([1-12]):?([0-5]\d)?\s(am|AM|pm|PM)\sto\s([1-12]):?([0-5]\d)?\s(am|AM|pm|PM)', s):
        if (match.group(2) and match.group(5)) == None:
            min1 = "00"
            min2 = "00"
        elif match.group(2) == None:
            min1 = "00"
            match.group(5) = min2
        elif match.group(5) == None:
            match.group(2) = min1
            min2 = "00"


        if match.group(3) == ('PM' or 'pm'):
            if match.group(1) == '12':
                hour2 = '00'
            else:
                hour2 = match.group(4)
            hour1 = match.group(4)
            min1 = m



        else:
            ...
    else:
        raise ValueError("ValueError")

    return f"{}:{} to {}:{}"




if __name__ == "__main__":
    main()
