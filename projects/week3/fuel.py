def main():
    fuel = input("Fraction: ")
    final = run(fuel)

    if final > 1:
        main()
        return
    elif final == 1:
        print("F")
    elif final == 0:
        print("E")
    else:
        print(final,"%")

def run(str):
    n,d = str.split('/')
    try:
        n = int(n)
        d = int(d)
        return (n/d)*100
    except (ValueError, ZeroDivisionError):
        main()
        return

main()
