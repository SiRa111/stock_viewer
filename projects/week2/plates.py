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
    for i in range(len(l)):
        c = 0
        while c < 3:
            c += 1
            if l[i].isalpha() :
                print(l[i])
                continue
            else:
                return False
    '''
    c2(s)
    c3(s)
    c4(s)
    '''

def c1(string):
    l = []
    for i in range(len(string)):
        l.append(string[i])
    for i in range(len(l)):
        if l[i].isalpha() :
            print(l[i])
            continue
        else:
            return False



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
