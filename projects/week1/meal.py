
def main():
    t = input("Enter the time in 24hr or 12hr format: ")


    if t.endswith("am" or "a.m." or "A.M." or "a.m" or "A.M") :
        t = convert(t)
        t = final(t)
    elif t.endswith("pm" or "p.m." or "P.M." or "p.m" or "P.M") :
        t = time(t)
        t = final(t)
    else :
        t = convert(t)
        t = final(t)

def final(k):
    if 7.00 <= k <= 8.00:
        print("breakfast time
    elif 12.00 <= k <= 13.00:
        print("lunch time")
    elif 18.00 <= k <= 19.00:
        print("dinner time")

def time(t):
    m,n = t.split(' ')

    c,d = m.split(":")
    c = float(c)
    d = float(d)
    d = d * 0.0167

    c = 12 + c
    c = c + d
    c = "{:.2f}".format(c)
    c = float(c)

    return c

def convert(t):
    m = t.rstrip(' ')

    a,b = m.split(":")  #splits time in hours and minutes
    b = float(b)
    b = b * 0.0167
    a = float(a)

    a = a + b
    a = "{:.2f}".format(a) #gives two decimal points to a and turns it to a string as this is a f string
    a = float(a)

    return a


if __name__ == "__main__":
    main()

