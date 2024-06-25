'''
CONDITIONALS allow the program to make a desicion

if x < y
x < y is a boolean ie true or false value

if x < y :          statement 1
    print("yay")
if x > y:           statement 2
    print("welp")
if x == y:          statement 3
    print("um")

each time  the if condition is run. ie if statement 1 is true the code runs then the second statement is also checked and the third too. similarly even if it were false all the three statements would be checked. for a program conssisting if billions of lines of code. this slows down the process so we make our code more efficient :

if x > y:               s1
    print("yay")
elif x < y:             s2
    print("welp")
else :                  s3
    print("x == y ")

now if statement one is true the rest are ignored. the execution only proceeds if the statement is false.

0 OR
you can enter more than one condtion to check
if x < y or x > y:
we are checking both. if either is true, the code will run

more efficient way :
if x != y:

0 AND
it checks more than two statements simultaneously. code is only executed if all the conditions are met
if score >= 90 and score <= 100:

more efficient :
90 <= score <= 100:

0 parity refers to whether a number is either even or odd.

0 MATCH
 name = input("What's your name? ")

  match name:
      case "Harry" | "Hermione" | "Ron":
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _:
          print("Who?")

STRINGS ARE IMMUTABLE
ANY CHANGES MADE IN STRINGS ARE TRANSIENT


'''
