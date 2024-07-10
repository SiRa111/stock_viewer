import emoji

def main():
  i = input("Input: ")
  emo(i)

def emo(string):
  a,b = string.lstrip(":")
  print(a,b)


main()
