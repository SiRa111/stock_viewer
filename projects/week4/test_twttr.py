from twttr import shorten


def main():
  string = input("string here : ")
  a = shorten(string)
  final=""
  for _ in a:
    final = final + _
  print(final)
  return True
main()

