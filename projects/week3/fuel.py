def main():
    fuel = input("Fraction: ")
    n,d = fuel.split('/')
    n = int(n)
    d = int(d)
    final = run(n,d)

    if final > 1:
        main()
        return
    elif final == 1:
        print("F")
    elif final == 0:
        print("E")
    else:
        print(final)

def run(a,b):
    try:
        return int(a/b)
    except (ValueError, ZeroDivisionError):
        main()
        return

main()
