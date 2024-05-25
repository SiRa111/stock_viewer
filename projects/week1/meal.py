def main():
    t = input("Enter the time in 24hr format or 12 hr format : ")
    convert(t)


def convert(time):
    def c(t):
        t = t.rstrip(" ")
        t1, t2 = t.split(":")
        
    if time.endswith("a.m" or "p.m."):
        c(time)

if __name__ == "__main__":
    main()
