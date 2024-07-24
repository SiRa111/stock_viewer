import sys


def main():
    if len(sys.argv) == 1:
        print("Too few commnad-line arguments")
        sys.exit(1)
    elif len(sys.argv) >= 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif sys.argv[0].endswith(".py") :
        if sys.argv[1].endswith(".py"):
            try:
                count(sys.argv[1])
            except FileNotFoundError:
                print("File does not exist")
                sys.exit(1)
        else:
            print("Not a Python file")
            sys.exit(1)


def count(filename):
    with open("memo.txt", "w") as file:
        with open(f"{filename}", "r") as _:
            om = _.readlines()
            for whoa in om:
                whoa = whoa.lstrip()
                file.write(whoa)


    i = 0
    with open("memo.txt", "r") as filo:
        readlist = filo.readlines()
        for _ in readlist:
            if _.startswith("#"):
                continue
            elif _.startswith("\n"):
                continue
            elif _.startswith("\t"):
                continue
            elif _.isspace():
                continue
            elif _ == "":
                continue
            else:
                i = i + 1
    print(i)


if  __name__ == "__main__":
    main()
