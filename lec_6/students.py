import csv

name = input("Whats your name? ")
home = input("Where is your home? ")

with open("students.csv", "a") as file:
  writer = csv.DictWriter(file, fieldnames=["name","home"])
  #fieldnames are the arguments to dict writer
  writer.writerow({"name":name, "home":home})
