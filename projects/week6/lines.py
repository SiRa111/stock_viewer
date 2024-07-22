import sys


def main():
    if len(sys.argv) == 1:
        print("Too few commnad-line arguments")
        sys.exit()
    elif len(sys.argv) >= 3:
        print("Too many command-line arguments")
        sys.exit()
    else:
        if '.py' in sys.argv[1]:
            count(sys.argv[1])
        else:
            print("Not a Python file")
            sys.exit()


def count(filename):
    with open("memo.txt", "a") as file:
        for _ in filename:
            file.write(f"{_}\n")


if  __name__ == "__main__":
    main()
