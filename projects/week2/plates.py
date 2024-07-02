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

    if 2 <= len(l) <= 6:
        print(len(l))
        pass
    else:
        return False


    if len(l) >= 2:
        for i in range(2):
            if l[i].isalpha():
                continue
            else:
                return False


    for i in range(len(l)):
        if l[i].isalnum():
            continue
        else:
            return False


    e=[]
    for i in range(len(l)):
        if l[i].isnumeric():
            e.append(l[i])
            if e[0] == '0':
                return False

   
    digits=[]
    num_index = int()
    for i in range(len(l)):
        if l[i].isalpha():
            continue
        elif l[i].isnumeric():
            num_index = i
            break

    digits = l[num_index:]

    for i in digits:
        if i.isalpha():
            return False

    return True












main()
