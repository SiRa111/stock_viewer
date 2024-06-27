def main():
    str = input("Enter string in camelCase : ")
    final = snake(str)
    print(final)

def snake(string):
    for i in string:
        a = ""
        if "A" <= i <= "Z":
            i = "_" + i.lower()
        else:
            pass

        a += i
    return a
main()
