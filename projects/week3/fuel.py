def main():
    fuel = input("Fraction: ")
    final = run(fuel)

    if final > 100:
        main()
        return
    elif 90 < final <= 100:
        print("F")
    elif 0.01 <= final <= 10:
        print("E")
    else:
        print(f"{final}%")

def run(str):

    try:
        n = int(n)
        d = int(d)
        s = float((n/d))
        return s*100

    except (ValueError, ZeroDivisionError):
        main()
        return

main()
