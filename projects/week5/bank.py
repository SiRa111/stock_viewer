def main():
    if g1.startswith("hello"):
        return "$0"
    elif g1.startswith("h"):
        return "$20"
    else:
        return "$100"

def value(greeting):
    g = input("Greeting : ")
    g1 = g.strip().lower()


a = main()
print(a)

