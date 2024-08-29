import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    match = re.search(r'([1-9]|1[0-2]):?([0-5]\d)?\s*(AM|PM)\s*to\s*([1-9]|1[0-2]):?([0-5]\d)?\s*(AM|PM)', s, re.IGNORECASE)

    if match:
        hour1, min1, period1, hour2, min2, period2 = match.groups()


        hour1 = int(hour1)
        hour2 = int(hour2)

        if period1.lower() == 'pm' and hour1 != 12:
            hour1 += 12
        elif period1.lower() == 'am' and hour1 == 12:
            hour1 = 0

        if period2.lower() == 'pm' and hour2 != 12:
            hour2 += 12
        elif period2.lower() == 'am' and hour2 == 12:
            hour2 = 0


        if not min1:
            min1 = "00"
        if not min2:
            min2 = "00"

        return f"{hour1}:{min1} to {hour2}:{min2}"

    else:
        raise ValueError("ValueError")

    

if __name__ == "__main__":
    main()
