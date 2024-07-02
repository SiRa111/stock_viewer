'''
print("meow")
print("meow")
print("meow")
'''
# to print meow 3 times but what if 1000 times

'_____WHILE LOOP______'
'''
i = 3                               1
while i != 0:                       2
    print("meow", end = " ")        3
'''
#this sets up an infinite loop as i will always be 3
#thus statement 2 will always be true
#flow : 2 > 3 > 2 > 3 > 2 > 3 ...
#happens because we are not altering the value of i


'''
i = 3
while i != 0:
    print("meow")
    i = i - 1   | i -= 1
'''
#decerementing the value  of i


'''
i = 0
while i < 3:       #going upto 3 but not through 3
    print("meow")
    i = i + 1    |  i += 1
'''
#increment with i = 0


'''
i = 1
while i <= 3:      #going upto and through 3
    print("meow")
    i = i + 1    |  i += 1
'''
#increment with i = 1


'___LIST___'



'___FOR LOOP___'
#for loop lets you iterate through a list of items
#use for loop when you know the termination number
'''
for i in [0, 1, 2]: #but what if there were a million values
    print("meow")
'''

'''
for i in range(3):   #we use range fxn here
    print("meow")

range always takes INTEGER values

ALSO we have i here but we are not using it. better code :
for _ in range(3):      #replace i with _
    print("meow")
'''

'''
range(3) means loop will execute 3 times.
values : 0 1 2
'''

'''
print("meow\n" * 3)
meow
meow
meow

___this is the output. we dont want the last space.

print("meow\n" * 3, end="")
meow
meow
meow
___the string ends without any space.
'''

# USE WHILE LOOP WHEN YOU WANT THE PROGRAM TO MEET CERTAIN EXPECTATION
'''
if i want to take input of only positive integers

i = input("Enter a number : ")
if i < 0:
    i = input("Enter a number : ")
    if i < 0 :
        i = input("Enter a number : ")
        if i < 0:
            i = input("Enter a number : ") ...
            .
            .
            .
Hence we would keep on writing an infinite loop.
EXPECTATION : take only positive integers

using while loop :

while True:             #1
    n = int(input("Enter a number : ")) #2
    if n < 0:           #3
        continue        #4 breaks current iteration and returns to the beginning of the loop ie 1 for next iter
    else:               #5
        break           #6 breaks the loop iteration and brings us out of the loop

        #pass : nothing happens.

better code :


___Printing meow by taking no as input from the user__

while True: #1
    n = int(input("Enter the value of n : ")) #2
    if n > 0:   #3
        break   #4

for _ in range(n):
    print("meow")

negative int : 1 2 1 2 1 2 1 2 ...
postivive int : 1 2 3(statement true) 4 and comes out of the loop


'''
# while True :
#this sets up an infinite loop


#___PRINTING MEOWS BY DEFINING FXNS__
'''
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:         #infinite loop set
        a = int(input("Enter the number : "))
        if a > 0:
            return a    #if a positive value is given it is returned and the loop ends

def meow(n):
    for i in range(n):
        print(i + 1, "meow")

main()

you can print multiline text by:

def function_name():
    return f"""
--------------------------------------
ANY TEXT WITHIN THIS WILL GIVE THE MULTILINE OUTPUT

__________________________________________________

"""

print(function_name)

'''
dic = {"name":"name1", "id":"001"}
dic["address"] = "ghar"
dic["address"] = "ghar"

print(dic["name"])
print(dic["id"])
print(dic["address"])
# KeyError : address
#to handle that we give a default value


#OTHER DICT METHODS
print(f"random shit :{dict["name"]}")
print(f"random shit : {dict.get("UWU", "default_value")}")
#if the key does not exist the default value will be printed
dict.update({"mother_name":"maa ka naam", "fathers name" : "sperm donour"})
