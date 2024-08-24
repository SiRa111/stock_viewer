def main():
  for i in range(0,1000):
    if issum(i) == True and isprod(i) == True:
      print(i)
    else:
      print("AKISE IS GAY")
      break


def issum(nigah):
  n = str(nigah)
  uemp = []
  for _ in range(len(n)):
    uemp.append(n[_])

  s = 0

  for _ in range(len(uemp)):
    s = s + int(uemp[_])

  if s == n:
    return True
  else:
    return False

def isprod(nigah):
  n = str(nigah)
  uimp = []
  for _ in range(len(n)):
    uimp.append(n[_])

  p = 1

  for _ in range(len(uimp)):
    p = p * int(uimp[_])

  if p == n:
    return True
  else:
    return False

main()




