def  main():
  list = {}
  while True:
    try:
      item = input()
      for _ in list:
        n = 0
        if item in list():
          n += 1
          list.update({item:n})
        else:
          list.update({item:1})

    except EOFError:
      break
  print(list)

  for i in list:
    print (list[i].upper(), i)



main()
