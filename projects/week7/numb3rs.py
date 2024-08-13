import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    if re.search(r"^(1/d|2[012345])\d$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
