import emoji

def main():
  i = input("Input: ")
  emo(i)

def emo(string):
  for _ in emoji:
    print(_)

main()
