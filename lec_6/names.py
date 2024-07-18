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
