'''modules also known as libraries encourage reusablity of code
'''

# 0 random
___random.choice(seq)
the seq will be a sequence.
eg: list, string
the choice will be made from the elements of the sequence

** if youre using from
syntax:
coin = choice(['a','b'])

___random.randint(a,b)
it picks a random int bw a and b.
a and b are inclusive

___random.shuffle(x)
shuffles or randomizes the provided values. it does not return a specific value unlike the previous two methods, rather shuffles the entire list


# 0 statistics
mean - gives the average


# 0 sys
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
