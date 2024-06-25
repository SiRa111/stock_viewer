#FUNCTIONS can either
# 1. have an outcome
# 2. return a value which can be stored for further use

def greet(input):
    if "hello" in input:
        print("hello, there")
    else:
        print("I'm not sure what you mean")

greet("hello, jarvis ")

#--------------------------------------------------------------

def greets(input):
    if "hello" in input:
        return "hello, there."
    else:
        return "I'm not sure what you mean"

greets("hello jaaaaarvissssssssss")

#return statement STORES "hello, there" in the fxn calling.
#we need to print this now

print( greets("hello , jarvis  "))

z = greets("hello jaaaaarvissssssssss")
print(z + " xirae")




