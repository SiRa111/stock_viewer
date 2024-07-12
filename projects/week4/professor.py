import random


def main():
    get_level()


def get_level():
    while True:
        try:
            lev = int(input("Level: "))
            if 1 <= lev <= 3:
                generate_integer(lev)
            else:
                pass

        except ValueError:
            pass


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
