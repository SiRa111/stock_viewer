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

    print(l)
    
    d = 0
    for i in range(len(l)):
        print(i)

        '''
        d += 1
        if 2 <= d <= 6:
            return True
        else:
            return False
        '''









main()
