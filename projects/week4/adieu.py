def main():
  l = ["Adieu, ", "adieu, ", "to "]
  while True:
    try:
      name = input("Name: ")
      l.append(name)
    except EOFError:
      return l

a = main()
print(a)
