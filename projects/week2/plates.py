def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    c1(s)
    '''
    c2(s)
    c3(s)
    c4(s)
    '''

def c1(string):
    l = []
    for i in range(len(string)):
        l.append(string[i])
    for i in range(2):
        if l[i].isalpha() :
            print(l[i])
            continue
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
