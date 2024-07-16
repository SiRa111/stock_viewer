def main():
    fuel = input("Fraction: ")
    final = run(fuel)


def convert(str):
    try:
        n,d = str.split('/')
        n = int(n)
        d = int(d)
        s = float((n/d))
        s = round(s*100)
        return s

    except (ValueError, ZeroDivisionError):
        main()
        return

def gauge(percentage):
    if final > 100:
        main()
        return
    elif 90 < final <= 100:
        print("F")
    elif 0.01 <= final <= 10 or final == 0:
        print("E")
    else:
        print(f"{final}%")


if __name__ == "__main__":
    main()
