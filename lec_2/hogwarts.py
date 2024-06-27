'''

students = ["Hermionie", "Harry", "Ron"]


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


#_________DICTIONARY___________
students = {
    "Hermionie" : "Gryffindor", #key : value pair
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"
}


Printing the values wrt their keys - HARDCODED
print(students["Hermionie"]) --> Gryffindor
print(students["Harry"])     --> Gryffindor
print(students["Ron"])      --> Gryffindor
print(students["Draco"])     --> Slytherin



#BY DEFAULT - FOR LOOP ITERATES ONLY THE KEYS

for key in students:
    print(key, students[key], sep=", ")
         #key  value


OP
Hermionie
Harry
Ron
Draco
'''

#********************************************************
#for loop iterates over the index in a list
'''

l = ["Hermionie", "Harry", "Ron", "Draco"]

for i in range(len(l)):
    print(i, l[i])
    #iterates over the index

for i in l:
    print(i)
    #iterates over the elements

#it iterates over the key in dictionary


'''
