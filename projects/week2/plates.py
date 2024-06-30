def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    c1(s)


def c1(s):
    l = []
    for i in range(len(s)):
        l.append(s[i])
    if len(l) >= 2:
        for i in range(2):
            if l[i].isalpha():
                continue
            else:
                return False
    else:
        return False
    return True




def c2(string):
    l = []
    for i in range(len(string)):
        l.append(string[i])
    print(l)
    d = 0
    for i in range(len(l)):
        print(i)
        if 2 <= d <= 6:
            return True
        else:
            return False


main()
