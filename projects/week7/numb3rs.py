import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    if re.search(r"^[0-3]\.[2-5]\.[4-9]\.[6-10]$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
