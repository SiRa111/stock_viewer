def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    l = []
    for i in range(len(s)):
        l.append(s[i])

    c = 0
    while c < 2:
        if l[i].isalpha() :
            c += 1
            return True
        else:
            return False

    d = 0
    while 2 <= d <= 6:
        d += 1
        return True
    









main()
