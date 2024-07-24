import sys
import csv

def main():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv"):
            try:
                pizza(sys.argv[1])
            except FileNotFoundError:
                print("File not found")
                sys.exit(1)
        else:
            print("Not a CSV file")
            sys.exit(1)

    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)


def pizza(csvfile):
    with open(f"{csvfile}", "r") as file:
        reader = DictReader(file)
        reader = readlines


if __name__ == "__main__":
    main()
