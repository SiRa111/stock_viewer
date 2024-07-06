def  main():
  list = {}
  while True:
    try:
      item = input()

      if item in list:
        n = list[item]
        list.update({item:n+1})
      else:
        list.update({item:1})

    except EOFError:
      break

  for _ in list:
    _ = _.upper()
    







main()
