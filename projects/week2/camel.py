def main():
    str = input("Enter string in camelCase : ")
    final = snake(str)
    print(final)

def snake(string):
    for i in string:
        if "A" <= i <= "Z":
            i = i.lower()

