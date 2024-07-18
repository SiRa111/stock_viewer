names = []
#a list to gather the txt data


with open("names.txt") as file: #default is r mode
  for line in file:
    names.append(line.rstrip()) #we dont want newlines


for name in sorted(names, reverse = True): #alphetically sorted list
  print(f"hello, {name}")
