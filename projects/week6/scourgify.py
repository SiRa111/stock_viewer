import csv
import sys


def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit()
    else:
        try:
            clean(sys.argv[1], sys.argv[2])
        except FileNotFoundError:
            print("File not found")
            sys.exit(1)


def clean(nsorted, sorted):
    ...



if __name__ == "__main__":
    main()
