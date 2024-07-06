def  main():
  list = {}
  while True:
    try:
      item = input()
      for _ in list():
        n = 0
        if item in list():
          n += 1
          list.update(item:n)
        else:
          list.update(item:1)

    except EOFError:
      break
  list = list.sort()
  for i in list:
    print(list[i], i)



main()
