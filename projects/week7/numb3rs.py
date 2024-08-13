import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    if re.search(r"^/d?/d|1/d/d|2[01234]/d|25[012345]$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
