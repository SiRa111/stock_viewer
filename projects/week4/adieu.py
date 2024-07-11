def main():
  l = ["Adieu, ", "adieu, ", "to "]
  try:
    while True:
      if len(l) < 4:
        name = input("Name: ")
        l.append(name)
      elif len(l) >= 4:
        name = input("Name: ")
        l.append(name+",")

  except EOFError:
    pass
  a = []
  a.append(l[-1])
  l.pop()
  l.append("and")
  l.append(a[0])
  return l

q = main()
for _ in q:
  print(_, end=" ")
print()
