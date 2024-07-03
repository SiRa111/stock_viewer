'''
try:
    x = int(input("Enter value for x : "))          #2
except ValueError:
    print("Your entered value is not an integer.")  #4

print(f"x is {x}")      #6


input: cat
ERROR RECEIVED : NameError
'x' is not defined

why: in line two int() fxn wants only int value but we enter a string. so a ValueError occurs first. due to this error on RHS in line2, no value was assigned to the variable called x.
Hence, x was never defined and therefore when we try to print it in line6. We get NameError.
'''
while True: #infinite loop that runs until an integer is entered
    try:
        x = int(input("Enter value for x : ")) #try this statement
    except ValueError:
        print("Your entered value is not an integer.") #if the specified error is raised. execute this statement
    else:
        print(f"x is {x}")
        #if no error is raised. execute the else block
        break
'''
flow of code :
input: cat --> 1 2 3 4. as cat would raise a valueError
input: 67  --> 1 2 5 6. as no error was raised. the else statement gets executed
'''

alternate code with lesser lines:

while True:
    try:
        x = int(input("Enter value for x : "))
        break
    except ValueError:
        print("Your entered value is not an integer.")

print(f"x is {x}")


#############################################################
even better code :

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("Enter the value of x : "))
        except ValueError :
            pass
            #the loop will keep on running till we get an int value

main()
