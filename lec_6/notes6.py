sorted(argument, key = None, reverse = False)
by default reverse is false
but if we want in descending order : reverse = True
list
tuple
different strings
integers


0 code to enter data in a file:


name = input("Whats your name? ")

'''
file = open("names.txt", "a") #append mode
file.write(f"{name}\n")
file.close()
'''

"""
METHOD WITH NO CLOSIGN TAG

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
"""


'''
#SORTING ON THE BASIS OF HOUSE
def get_house(student):
  return student["house"]

for student in sorted(students, key=get_house, reverse = True):
  print(f"{student['name']} is in {student['house']}")
'''

#___________USING LABDA FUNCTION___________________
for student in sorted(students, key=lambda student: student["name"]):
  print(f"{student['name']} is in {student['house']}")


LAMBDA FXN
it only needs to be called once
so we dont name it
anonymous


CSV MODULE
0 DictReader is robust. even though we might make changes to the csv file. it will understand :)
''' to read dict from a csv file

import csv


students = []


with open("students.csv") as file:
  reader = csv.DictReader(file) #dict reader
  for row in reader:
    students.append({"name": row["name"], "home":row["home"]})


for student in sorted(students, key=lambda student: student["name"]):
  print(f"{student['name']} is from {student['home']}")
'''

