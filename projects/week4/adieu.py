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
  a = []
  a.append(l[-1])
  l.pop()
  l.append([])

a = main()
for _ in a:
  print(_, end=" ")
print()
