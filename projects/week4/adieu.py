def main():
  l = ["Adieu, ", "adieu, ", "to "]
  try:
    while True:
      if len(l) < 4:
        name = input("Name: ")
        l.append(name)
      elif len(l) >= 4:
        name = input("Name: ")
        l.append(","+name)

  except EOFError:
    pass
  a = l[-2:-1]
  print(a)

a = main()
for _ in a:
  print(_, end=" ")
print()
