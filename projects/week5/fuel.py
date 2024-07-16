def main():
    fuel = input("Fraction: ")
    final = convert(fuel)


def convert(str):
    try:
        n,d = str.split('/')
        n = int(n)
        d = int(d)
        s = float((n/d))
        s = round(s*100)
        return s

    except (ValueError, ZeroDivisionError):
        if n > d :
            return ValueError
        elif y == 0 :
            return ZeroDivisionError

def gauge(percentage):
    if percentage > 100:
        main()
        return
    elif 99 <= percentage:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
