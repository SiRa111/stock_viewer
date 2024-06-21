def main():
    t = input("Enter the time in 24hr format: ")
    convert(t)


def convert(time):
    a,b = split.time(":")
    b = b * 0.0167
    a = a + b
    



if __name__ == "__main__":
    main()
