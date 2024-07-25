import csv
import sys


def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        one = sys.argv[1]
        two = sys.argv[2]
        try:
            if one.endswith(".csv") and two.endswith(".csv"):
                clean(one, two)
            else:
                print("Not a csv file")
                sys.exit(1)
        except FileNotFoundError:
            print("File not found")
            sys.exit(1)


def clean(nsorted, sorted):
    with open(nsorted, "r") as ofile:
        reader = csv.reader(ofile)
        l=[]
        for _ in reader:
            try :
                last, first = _[0].split(",")
                last = last.strip()
                house = _[1]
                l.append(f"{first}, {last}, {house}")
            except:
                pass
    with open(sorted, "w") as sfile:
        writer = csv.writer(sfile, delimiter = "\n")
        writer.writerow(l)


if __name__ == "__main__":
    main()
