def  main():
  list = {}
  while True:
    try:
      item = input()
      list.update({item:1})
      if item in list:
        n = list[item]
        list.update({item:n+1})

    except EOFError:
      break
  print(list)





main()
