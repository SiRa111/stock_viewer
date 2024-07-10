def main():
  l = ["Adieu, ", "adieu, ", "to "]
  try:
    while True:
      if len(l) < 4:
        name = input("Name: ")
        l.append(name)
      elif len(l) >= 4:
        name = input("Name: ")
        l.append(name)
        l.append([-2],"and")


  except EOFError:
    return l

a = main()
for _ in a:
  print(_, end=" ")
print()
