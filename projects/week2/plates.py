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

    for i in range(2):
        if i.isalpha() :
            return True
        else:
            return False







main()
