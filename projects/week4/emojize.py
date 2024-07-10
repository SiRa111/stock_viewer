import emoji

def main():
  i = input("Input: ")
  emo(i)

def emo(string):
  print(emoji.emojize(":thumbsup:"))

main()
