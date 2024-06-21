def main():
    t = input("Enter the time in 24hr format: ")
    convert(t)


def convert(time):
    a,b = time.split(":")  #splits time in hours and minutes
    b = float(b)
    b = b * 0.0167
    a = float(a)
    a = a + b
    a = "{:.2f}".format(a) #gives two decimal points to a and turns it to a string as this is a f string
    a = float(a)
    print(a)

'''
    if 7.00 <= a <= 8.00:
        print("breakfast time")
    elif 12.00 <= a <= 13.00:
        print("lunch time")
    elif 18.00 <= a <= 19.00:
        print("dinner time")
'''

if __name__ == "__main__":
    main()

