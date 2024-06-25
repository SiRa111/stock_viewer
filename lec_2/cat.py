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
'''

'''
range(3) means loop will execute 3 times.
values : 0 1 2
'''
