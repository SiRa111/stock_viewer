import emoji

def main():
  i = input("Input: ")
  emo(i)

def emo(string):
  if '_' in string:
    print(emoji.emojize(f"{string}"))
  elif '_' not in string:
    print(emoji.emojize(f"{string}", language= 'alias'))


main()
