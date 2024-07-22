import sys


def main():
    if len(sys.argv) == 1:
        print("Too few commnad-line arguments")
        sys.exit(1)
    elif len(sys.argv) >= 3:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        if '.py' in sys.argv[1]:
            count(sys.argv[1])
        else:
            print("Not a Python file")
            sys.exit(1)


def count(filename):
    with open("memo.txt", "a") as file:
        with open(f"{filename}", "r") as _:
            om = _.readlines()
            for whoa in om:
                file.write(whoa)

    i = 0
    with open("memo.txt", "r") as filo:
        readlist = filo.readlines()
        for _ in readlist:
            if _.startswith(" "):
                continue
            elif _.startswith("#"):
                continue
            elif _.startswith(" #"):
                continue
            else:
                i = i + 1
    print(i)


if  __name__ == "__main__":
    main()
