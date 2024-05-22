g = input("Greeting : ")
g1 = g.strip().lower()

def main():
    if g1.startswith("hello"):
        return "$0"
    elif g1.startswith("h"):
        return "$20"
    else:
        return "$100"

a = main()
print(a)

