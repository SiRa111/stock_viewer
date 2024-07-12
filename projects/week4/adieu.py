def main():
  l = ["Adieu,", "adieu,", "to"]
  try:
    while True:
        name = input("Name: ")
        l.append(name+",")

  except EOFError:
    pass

  e = []
  e.append(l[-1])
  e[-1].rstrip(",")
  print(e)
  if len(l) < 6:
    match len(l):
      case 4:
        l.pop()
        l.append(e[-1])
      case 5:
        e.append[-2]
        e[-2].rstrip(",")
        l.pop()
        l.pop()
        l.append(e[-2])
        l.append("and")
        l.append(e[-1])
  else:
    l.pop()
    l.append("and")
    l.append(e[-1])
  return l

q = main()
for _ in q:
  print(_, end=" ")
print()
