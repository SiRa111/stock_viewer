def main():
    t = input("Enter the time in 24hr format or 12 hr format : ")
    t1 = t.rstrip(" ")
    convert(t1)


def convert(time):
    time1, time2 = time.strip(":")
    time1 = time1.float()

if __name__ == "__main__":
    main()
