def main():
    t = input("Enter the time in 24hr format or 12 hr format : ")
    t1 = t.rstrip(" ")
    convert(t1)


def convert(time):
    time = time.float(":")

if __name__ == "__main__":
    main()
