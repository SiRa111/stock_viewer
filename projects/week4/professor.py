import random


def main():
    final = get_level()
    print(final)


def get_level():
    ans = int()
    while True:
        try:
            lev = int(input("Level: "))
            if 1 <= lev <= 3:
                ans = generate_integer(lev)
                break
            else:
                pass

        except ValueError:
            pass
    return ans


def generate_integer(level):
    s = 0
    if level ==  1:
        for _ in range(10):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            s = game(x, y, s)

    elif level == 2:
         for _ in range(10):
            x = random.randint(10, 99)
            y = random.randint(10, 99)
            s = game(x, y, s)

    elif level == 3:
         for _ in range(10):
            x = random.randint(100, 999)
            y = random.randint(100, 999)
            s = game(x, y, s)
    else:
        pass
    return s


def game(a, b, score):
    i = 0
    while i < 3:
        try:
            sum = int(input(f"{a} + {b} = "))
            if sum == a + b:
                score += 1
                break
            elif sum != a + b and i < 2:
                print("EEE")
                i += 1
            elif i == 2:
                i = 0
                print(f"{a} + {b} = {a+b}")
                break
        except ValueError:
            if i < 2:
                i += 1
            elif i == 2:
                print(f"{a} + {b} = {a+b}")
                break
    return score


if __name__ == "__main__":
    main()
