students = ["Hermionie", "Harry", "Ron"]

'''
print(students[0])
print(students[1])
print(students[2])


for student in students:
    print(student)
print("-----")

for i in range(3):
    print(students[i])
print("-----")

#len(students)  --> this gives us the length of the list students

for i in range(len(students)):
    print(i + 1, students[i])
'''

#_________DICTIONARY___________
students = {
    "Hermionie" : "Gryffindor",,  #key : value pair
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"
}

'''
Printing the values wrt their keys - HARDCODED
print(students["Hermionie"]) --> Gryffindor
print(students["Harry"])     --> Gryffindor
print(students["Ron"])      --> Gryffindor
print(students["Draco"])     --> Slytherin
'''

#BY DEFAULT - FOR LOOP ITERATES ONLY THE KEYS

for i in students:
    print(i, students[i])
         #key  value

'''
OP
Hermionie
Harry
Ron
Draco
'''
