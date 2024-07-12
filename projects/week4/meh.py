match [1, 2]:
  case (a, b, c):
    print(a, b, c) # wont run
  case (x):
    print(x) # will run
  case (a, b):
    print(a, b) # should run but maybe x will eat it first
