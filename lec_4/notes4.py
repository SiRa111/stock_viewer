'''modules also known as libraries encourage reusablity of code

import downloads the entire library

if you use from you download that specified fxn
syntaxz;

from random import shuffle()
this will just download the shiffle fxn
'''

# 0 random
___random.choice(seq)
the seq will be a sequence.
eg: list, string
the choice will be made from the elements of the sequence

** if youre using from
syntax:
coin = choice(['a','b'])


___random.choices(list_name, k=2)
k is the no. of random elements from that list
shuffling with replacement
choose a card. write it down. put it back. choose again
for [1,2,3]: [1,1]... may happen

___weighing the choices
cards = ["jack", "king", "queen"]
random.choices(list_name, weights=[100,0,0]k=2)
#the weights are entred according to the index of the list
#here the output will always be [jack,jack]
sum of weights = 100
weights=[5,20,75]


___random.sample(list_name, k=2)
shuffling without replacement
[1,2,3] : [2,2]... twin cases will never occur

___random.randint(a,b)
it picks a random int bw a and b.
a and b are inclusive

___random.shuffle(x)
shuffles or randomizes the provided values. it does not return a specific value unlike the previous two methods, rather shuffles the entire list


# 0 statistics
mean - gives the average


# 0 sys - library
__sys.argv - argument vector
stores the data entered in the command line even before the program is executed
by default index 0 holds the name of the file being executed
eg : name.py
index 1 holds what we input after file name
eg : python name.py Simran <-- cmd line text
name.py is in sys.argv[0]
Simran is stored in sys.argv[1]

__sys.exit - exits the command line


#iterating over the list here
for arg in sys.argv[1:]: #slicing the list here. printing from index 1
  print("My name is",arg)

__
[1:] from index one till end. 1 included
[1:-1] from index 1 till the last index. LAST EXCLUDED


#PACKAGES
3rd party libraries to gain more functionalities

pip: package manager
allows you to install packages and softwares by the command  line
which do not come pretinstalled with python
eg : pip install figlet
pip install emoji
pip install cowsay

eg: requests library


APIs: application programming interface
3rd party services
a mechanism whereby you can access data on someone else's server and itegrate it to my own program

requests: allows us to make web requests (library)
allows your program to behave as a web browser would.

JSON: javascript object notation
used as language agnostic format ie you can use any programming language to read or write json

#json library -- comes with python
so no need to install with pip
json.dumps() - prints the the request data in more aethetic manner (more comfortrable to eyes)


(__name__)
n Python, __name__ is a special built-in variable. When a Python file is run directly, __name__ is set to "__main__". However, if the file is imported as a module in another Python script, __name__ is set to the name of that module (the filename without the .py extension). This allows you to have parts of your code which only run when the file is executed directly, and not when it's imported as a module. This is often used to write test code or to run a function when the file is executed directly.

random.seed(0)
random.seed(1)
a random output will be generated for the seed.
if the seed is same, output is same
used to debug

by dafault the seed for various fxn is something like systemtime.
