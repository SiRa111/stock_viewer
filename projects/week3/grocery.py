def  main():
  listd = {}
  dict={}
  while True:
    try:
      item = input()

      if item in listd:
        n = listd[item]
        listd.update({item:n+1})
      else:
        listd.update({item:1})

    except EOFError:
      break

  l = list(listd.keys())
  l.sort()
  print(l)
  '''
  for _ in listd:
    _ = _.upper()
  '''








main()
