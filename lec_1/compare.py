x = int(input("Enter the value for x : "))
y = int(input("Enter the value for y : "))

def main():
    if x < y:
        return "x is less than y."
    elif x > y:
        return "x is greater than y."
    else:
        return "x is equal to y."

a = main()

def main1():
    if x != y:
        return "x is not equal to y"
    else:
        return "x is equal to y"

b = main1()
print(b)
