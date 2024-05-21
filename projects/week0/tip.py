def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d1 = d.lstrip('$')
    d2 = float(d1)
    print(d2)
    return d2


def percent_to_float(p):
    p1 = p.rstrip('%')
    p2 = float(p1)
    p3 = p2*0.01
    print(p3)
    return p3


main()
