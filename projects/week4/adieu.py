def main():
  l = ["Adieu,", "adieu,", "to"]
  try:
    while True:
        name = input("Name: ")
        l.append(name+",")

  except EOFError:
    pass

  return l

q = main()
for _ in q:
  print(_, end=" ")
print()
