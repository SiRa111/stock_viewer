def main():
    fuel = input("Fraction: ")
    n,d = fuel.split('/')
    final = run(n,d)
    print(final)

def run(a,b):
    try:
        return int(a/b)
    except (ValueError, ZeroDivisionError):
        main()
        return

main()
