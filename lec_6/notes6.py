sorted(argument)
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
