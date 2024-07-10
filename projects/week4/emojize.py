import emoji

def main():
  i = input("Input: ")
  emo(i)

def emo(string):
  a,b = string.split(":",1)
  b = ":" + b
  if '_' in b:
    print(emoji.emojize(f"{a} {b}"))
  elif '_' not in b:
    print(emoji.emojize(f"{a} {b}", language= 'alias'))

if __name__ == "__main__":
  main()
