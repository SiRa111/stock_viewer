import random


def main():
    final = get_level()
    print(final)


def get_level():
    while True:
        try:
            lev = int(input("Level: "))
            if 1 <= lev <= 3:
                ans = generate_integer(lev)
                return ans
            else:
                pass

        except ValueError:
            pass


def generate_integer(level):
    score = 0
    match level:
        case 1:
            for i in range(10):
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                i = 0
                while i < 3:
                    try:
                        sum = int(input(f"{x} + {y} = "))
                        if sum == x + y:
                            score += 1
                            break
                        elif sum != x + y and i < 2:
                            print("EEE")
                            i += 1
                        elif i == 2:
                            i = 0
                            print(f"{x} + {y} = {x+y}")
                            break
                    except ValueError:
                        if i < 2:
                            i += 1
                        elif i == 2:
                            print(f"{x} + {y} = {x+y}")
                            break

        case 2:
            for i in range(10):
                x = random.randint(10, 99)
                y = random.randint(10, 99)
                i = 0
                while i < 3:
                    try:
                        sum = int(input(f"{x} + {y} = "))
                        if sum == x + y:
                            score += 1
                            break
                        elif sum != x + y and i < 2:
                            print("EEE")
                            i += 1
                        elif i == 2:
                            i = 0
                            print(f"{x} + {y} = {x+y}")
                            break
                    except ValueError:
                        if i < 2:
                            i += 1
                        elif i == 2:
                            print(f"{x} + {y} = {x+y}")
                            break

        case 3:
            for i in range(10):
                x = random.randint(100, 999)
                y = random.randint(100, 999)
                i = 0
                while i < 3:
                    try:
                        sum = int(input(f"{x} + {y} = "))
                        if sum == x + y:
                            score += 1
                            break
                        elif sum != x + y and i < 2:
                            print("EEE")
                            i += 1
                        elif i == 2:
                            i = 0
                            print(f"{x} + {y} = {x+y}")
                            break
                    except ValueError:
                        if i < 2:
                            i += 1
                        elif i == 2:
                            print(f"{x} + {y} = {x+y}")
                            break

    return score


if __name__ == "__main__":
    main()
