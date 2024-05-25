def main():
    t = input("Enter the time in 24hr format or 12 hr format : ")
    convert(t)


def convert(time):

    def c(t):
        t = t.rstrip(" ")
        t1, t2 = t.split(":")
        t1 = t1.float(0)
        t2 = t2.float(2)
        if t1 > 12:
            t1 = t1 + 12
        else:
            pass
        t2 = t2 * 0.016
        tf = t1 + t2
        if tf >= 7 and tf <= 8:
            return "breakfast time"
        elif tf >= 12 and tf <= 13:
            return "lunch time"
        elif tf >= 16 and tf <= 17:
            return "dinner time"

    if time.endswith("a.m" or "p.m."):
        c(time)
    else:
        pass

    t1, t2 = time.split(":")
    print(t1)
    print(t2)
    t1 = t1.float(0)
    t2 = t2.float(2)
    t2 = t2 * 0.016
    tf = t1 + t2
    if tf >= 7 and tf <= 8:
        return "breakfast time"
    elif tf >= 12 and tf <= 13:
        return "lunch time"
    elif tf >= 16 and tf <= 17:
        return "dinner time"


if __name__ == "__main__":
    main()
