import random


def main():
    level = get_level()
    score = generate_integer(level)
    print(f"Score: {score}")


def get_level():
    ans = int()
    while True:
        try:
            lev = int(input("Level: "))
            if 1 <= lev <= 3:
                generate_integer(lev)
                break
            else:
                pass

        except ValueError:
            pass
    return lev


def generate_integer(level):
    print(level)
    s = 0
    try :
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
    except ValueError:
        pass

    return s


def game(a, b, score):
    i = 0
    while i < 3:
        if i == 2:
            i =  0
            print(f"{a} + {b} = {a+b}")
            break
        try:
            sum = int(input(f"{a} + {b} = "))
            if sum == a + b:
                score += 1
                break
            elif sum != a + b:
                print("EEE")
                i += 1

        except ValueError:
            i += 1


    return score


if __name__ == "__main__":
    main()
