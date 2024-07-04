def main():
    fuel = input("Fraction: ")
    final = run(fuel)

    if final > 100:
        main()
        return
    elif final == 100:
        print("F")
    elif final == 0:
        print("E")
    else:
        print(f"{final}%")

def run(str):
    n,d = str.split('/')
    try:
        n = int(n)
        d = int(d)
        return int((n/d)*100)
    except (ValueError, ZeroDivisionError):
        main()
        return

main()
