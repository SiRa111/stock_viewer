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

    #maximum six and minimum two characters
    if 2 <= len(l) <= 6:
        print(len(l))
        pass
    else:
        return False

    #checks if first two letters are alphabets.
    if len(l) >= 2:
        for i in range(2):
            if l[i].isalpha():
                continue
            else:
                return False

    #makes sure only digits and letters are entered
    for i in range(len(l)):
        if l[i].isalnum():
            continue
        else:
            return False

    #the first digit cannot be zero
    e=[]
    for i in range(len(l)):
        if l[i].isnumeric():
            e.append(l[i])
            if e[0] == '0':
                return False

    return True












main()
