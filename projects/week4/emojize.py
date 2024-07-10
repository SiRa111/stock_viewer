import emoji

def main():
  i = input("Input: ")
  emo(i)

def emo(string):
  if string in emoji:
    print(string)

main()
