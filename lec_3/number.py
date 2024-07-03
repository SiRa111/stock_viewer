try:
    x = int(input("Enter value for x : "))
    print(f"x is {x}")
except ValueError:
    print("Your entered value is not an integer.")
