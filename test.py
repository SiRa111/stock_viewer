
def main():
  for i in range(100):
    if issum(i) == True and isprod(i) == True:
      print(i)


def issum(n):
  uemp = []
  for _ in len(n):
    uemp.append(_)

  s = 0

  for _ in len(uemp):
    s = s + _

  if s == n:
    return True
  else:
    return False

def isprod(n):
  uimp = []
  for _ in len(n):
    uimp.append(_)

  p = 1

  for _ in len(uimp):
    p = p * _

  if p == n:
    return True
  else:
    return False

main()




