import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r'([1-12]):?([0-5]\d)?\s(am|AM|pm|PM)\sto\s([1-12]):?([0-5]\d)?\s(am|AM|pm|PM)', s):


        if match.group(3).lower() == 'pm':
            if match.group(1) == '12':
                hour2 = '00'
            else:
                hour2 = int(match.group(1)) + 12
            hour1 = match.group(4)
            min1 = match.group(5)
            min2 = match.group(2)

        else:
            if match.group(4) == '12':
                hour2 = '00'
            else:
                hour2 = int(match.group(4)) + 12
            hour1 = match.group(1)
            min1 = match.group(2)
            min2 = match.group(5)


        if (match.group(2) and match.group(5)) == None:
            min1 = "00"
            min2 = "00"
        elif match.group(2) == None:
            min1 = "00"
            min2 = match.group(5)
        elif match.group(5) == None:
            min1 = match.group(2)
            min2 = "00"

    else:
        raise ValueError("ValueError")

    return f"{hour1}:{min1} to {hour2}:{min2}"




if __name__ == "__main__":
    main()
