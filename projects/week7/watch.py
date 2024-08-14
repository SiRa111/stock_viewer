import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if valid := re.search(r"^https?://(?:www\.)youtube.com/embed/(z[a-zA-Z0-9]+)$", s):
        print()




if __name__ == "__main__":
    main()
