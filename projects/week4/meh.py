hello = "hello"
match "world":
  case hello:
    print("you should not have seen this")
    print(hello)
