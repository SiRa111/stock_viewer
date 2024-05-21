
'''
ls - lists all the files

cp - copies a file
# cp org_file.py new_file.py
cp indoor.py projects/indoor.py #making a new copy in another directory

mv - moves a file or rename
s it
mv goodbye.py farewell.py //renaming it to another file
mv farewell.py .. //moving the file out of the parent folder
mv indoor.py week0/indoor.py #moving it to diff directory
rm - removes a file
rm farewell.py

mkdir -  make a directory / folder

cd - change directory
cd folder/ {Both with or without the slashes is fine}

rmdir - remove a directory

clear - clears the terminal window #alt : l

'''


"""
TO DEFINE A FXN

def main():
    print("Heyyyyyyyyyyy, WOrldddddddddddd")
    print("ayassssssssssa. slayyyyyyyyyyyyyyyy")


"""


'''
VSC - text editor / compiler
top - text editor
bottom - terminal

To run code in terminal : python file_name.py

Functions - actions that the language already knows how to perform
eg - print, int, str

Variable - container for a value

num = 12
the value on rhs is assigned to the variable at the lhs

comments : #
"""any text bw these is a multiline comment"""

Pseudocode - explain each block of code for clarity


str - a sequence of text in python
arguments - factors that can influence the behaviour of the function
parameters - actual value passed to the function

default parameters for print() - sep=" ", end="\n" #brings the cursor to the new line after the string is printed


#SEP-SEP-SEP-SEP-SEP-SEP-SEP
print("a b c d e", sep="-") DOES NOT SEP AN ENTIRE STRING
op: a b c d e

print("a","b","c","d","e", sep="-") SEP THE VARIOUS STRS
op: a-b-c-d-e

escape sequence - \n for newline character
\" - to display " inside a string

FORMATTING STRINGS
# Ask the user for their name
name = input("What's your name? ")
print(f"hello, {name}")

String Methods

name = input("What's your name? ")
name = name.strip() #strips the spaces on the left and right side of the String

0 F-STRINGS
print(f"hello, {name}")

0 str.format()
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))

op: We are the knights who say Ni
op: spam and eggs

name.lstrip() : removes the spaces on the left side of the string
name.rstrip() : removes the spaces on the right side of the strip

0 name = name.capitalize()
simran rawat '-->' Simran rawat

0 name = name.title()
simran rawat '->' Simran Rawat

0 CONCISE CODE
name = name.strip().title()

0 MORE CONCISE
name = input("What's your name? ").strip().title()

0
#the user enters some string
#the string is saved in name variable
#the strins is striped off spaces on both sides
#the string is titled ie all the words of the string will be capitalized

0 SPLITTING STRINGS
a,b = name.split(" ")
split : divides the code into multiple strings based on the argument provided and saves in diff variables

0 typing - code file_name.py will automatically create that file
pressing tab after writing the code in interpreter. It autocompletes itself

0 INT
% - Modulus - gives remainder
int() - converts the data from string to int datatype

0 FLOAT
float(bleh)
returns value in floats

0 ROUND
round(number, ndigit=1/2/3)
3 means it will show till 3 deicmal places
# till what decimal place you want your number

#in programming languages, [] anything between these is generally optional so it will have a default value if a value is not specified

0 SYNTAX
z=1000000
print(z) --> 1000000
print(f"{z:,}") --> 1,000,000
print(f"{z:.2f}") --> specifying using fstring about how many decimal places to print. 2 in this case

0 def fxn():
to invent your own fucntion

def(parameter = "default value"):
this value will be printed when no other value is explicitly provided to the fxn

def hola():

0 SCOPE
If a fxn is defined within a fxn it can only be called within that fxn as its scope is within the fxn  and hence using it outside will give undefined

0 RETURN
passes back the value
ends the execution of the fxn call
any code after return is not considered
 [RETURN](calculator.py)





[FLOW](hello.py)

'''
#EMOJIS ARE JUST CHARACTERS !!
' You can save emojis as characters in python '
