def main():
  l = ["Adieu,", "adieu,", "to"]
  try:
    while True:
      if len(l) < 4:
        name = input("Name: ")
        l.append(name+",")
      elif len(l) >= 4:
        name = input("Name: ")
        l.append(name+",")

  except EOFError:
    pass
  if len(l) > 4:
    b = ""
    a = ""
    b = b + l[-1].rstrip(",")
    a = a + l[-2].rstrip(",")
    l.pop()
    l.pop()
    l.append(a)
    l.append("and")
    l.append(b)
  return l

q = main()
for _ in q:
  print(_, end=" ")
print()
