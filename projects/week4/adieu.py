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
  if len(l) < 6:
    match len(l):
      case 4:
        e[-1].rstrip(",")
      case 5:
        

  return l

q = main()
for _ in q:
  print(_, end=" ")
print()
