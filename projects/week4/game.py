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

def game(n):
  ans = random.randint(1,n)
  while True:
    try:
      guess = int(input("Guess: "))
      if guess < n and guess > 0:
        print("Too small!")
      elif guess > n and guess > 0:
        print("Too large!")
      elif guess == n:
        print("Just Right!")
        break
      else:
        pass
    except ValueError:
      pass


main()
