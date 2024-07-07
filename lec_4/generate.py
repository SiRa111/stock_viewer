import random
'''
MEthOD 1
import random
#youre importing all the functions from the random library

coin = random.choice(["heads", "tails"])
print(coin)


#METHOD 2
from random import choice

coin = choice(["heads","tails"])
print(coin)


number = random.randint(1,10)
print(number)
'''

cards = ["jack","queen","king"]
random.shuffle(cards)
for _ in cards:
  print(_)
