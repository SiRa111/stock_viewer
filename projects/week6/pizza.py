import sys
import csv
from tabulate import tabulate


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
        reader = csv.reader(file)
        head=[]
        feet=[]
        i = 0
        for _ in reader:
            if i == 0:
                head = _
                i += 1
            else:
                feet.append(_)
        print(tabulate( feet, head, tablefmt="grid"))


if __name__ == "__main__":
    main()
