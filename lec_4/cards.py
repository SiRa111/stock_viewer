import random

cards = ["jack", "king", "queen"]

def main():
  a = random.choices(cards, weights=[5,20,75], k=2)
  print(a)

main()
