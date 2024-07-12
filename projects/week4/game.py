import random


def main():
    while True:
        try:
            num = int(input("Level: "))
            if num > 0:
                game(num)
                break
            else:
                pass
        except ValueError:
            pass
    return


def game(n):
    ans = random.randint(1, n)
    print(ans)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < ans and guess > 0:
                print("Too small!")
            elif guess > ans and guess > 0:
                print("Too large!")
            elif guess == ans:
                print("Just Right!")
                return
            else:
                pass
        except ValueError:
            pass


main()
