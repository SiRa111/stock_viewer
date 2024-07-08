import sys

'''
final = "hello,my name is " + sys.argv[1]
print(final)
#if you dont input any value during the command you get IndexError
'''
try:
  print("hello, my name is", sys.argv[1])
except:
  print("Too few arguments")
