try:
    x = int(input("Enter value for x : "))          #2
except ValueError:
    print("Your entered value is not an integer.")  #4

print(f"x is {x}")      #6

'''
input: cat
ERROR RECEIVED : NameError
'x' is not defined

why: in line two int() fxn wants only int value but we enter a string. so a ValueError occurs first. due to this error on RHS in line2, no value was assigned to the variable called x.
Hence, x was never defined and therefore when we try to print it in line6. We get NameError.
'''
