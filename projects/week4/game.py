import random

def main():
  while True:
    num = int(input("Level: "))
    if num > 0:
      game(num)
      break
    else:
      pass

def game(n):
  ans = random.randint(1,n)
  while True:
    guess = int(input("Guess: "))
    if guess < n:
      print("Too small!")
    elif guess > n:
      print("Too large!")
    elif guess == n:
      print("Just Right!")
      break
    else:
      pass


main()
