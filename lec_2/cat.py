'''
print("meow")
print("meow")
print("meow")
'''
# to print meow 3 times but what if 1000 times

'''
i = 3                               1
while i != 0:                       2
    print("meow", end = " ")        3
'''
#this sets up an infinite loop as i will always be 3
#thus statement 2 will always be true
#flow : 2 > 3 > 2 > 3 > 2 > 3 ...
#happens because we are not altering the value of i

i = 3
while i != 0:
    i = i - 1
    print("meow")
     #decerementing the value  of i
