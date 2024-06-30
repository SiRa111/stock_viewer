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

    #checks if first two letters are alphabets
    if len(l) >= 2:
        for i in range(2):
            if l[i].isalpha():
                continue
            else:
                return False
    else:
        return False

    #maximum six and minimum two characters
    if 2 <= len(l) <= 6:
        print(len(l))
        pass
    else:
        return False

    e = []
    for i in range(len(l)):
        if l[i].isnumeric():
            e.append(l[i])
    print(e)

    return True












main()
