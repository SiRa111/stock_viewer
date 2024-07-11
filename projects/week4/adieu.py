def main():
  l = ["Adieu,", "adieu,", "to"]
  try:
    while True:
      if len(l) < 4:
        name = input()
        l.append(name+",")
      elif len(l) >= 4:
        name = input()
        l.append(name+",")

  except EOFError:
    pass
  if len(l) > 4:
    a = []
    a.append(l[-1].rstrip(","))
    l.pop()
    l.append("and")
    l.append(a[0])
  return l

q = main()
for _ in q:
  print(_, end=" ")
print()
