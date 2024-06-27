def main():
    str = input("Enter string in camelCase : ")
    final = snake(str)
    print(final)

def snake(string):
    for i in string:
        if "A" <= i <= "Z":
            i = "_" + i.lower()
        else:
            conntinue
        print(i, end="")

main()
