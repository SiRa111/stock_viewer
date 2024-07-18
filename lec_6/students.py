students = []

with open("students.csv") as file:
  for line in file:
    name, house = line.rstrip().split(",")
    student = {"name":name, "house":house}
    students.append(student)

#SORTING ON THE BASIS OF HOUSE
def get_house(student):
  return student["house"]

for student in sorted(students, key=get_house, reverse = True):
  print(f"{student['name']} is in {student['house']}")
