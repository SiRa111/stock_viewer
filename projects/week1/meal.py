def main():
    t = input("Enter the time in 24hr format: ")
    convert(t)


def convert(time):
    a,b = split.time(":")
    float(b) = b * 0.0167  #coverts b to string
    float(a) = a + b       #coverts a to string
    a = "{:.2f}".format(a) #gives two decimal points to a

    print(a)


if __name__ == "__main__":
    main()
