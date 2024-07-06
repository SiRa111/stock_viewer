def  main():
  list = {}
  while True:
    try:
      item = input()
      list.update({item:1})

    except EOFError:
      break
  print(list)

  



main()
