sorted(argument, key = None, reverse = False)
by default reverse is false
but if we want in descending order : reverse = True
list
tuple
different strings
integers


0 code to enter data in a file:


name = input("Whats your name? ")

'''
file = open("names.txt", "a") #append mode
file.write(f"{name}\n")
file.close()
'''

"""
METHOD WITH NO CLOSIGN TAG

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
"""


LAMBDA FXN
it only needs to be called once
so we dont name it
anonymous
