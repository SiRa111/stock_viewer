def main():
    str = input("Input: ")
    process(str)

def process(string):
    l = []
    for i in range(len(string)):

        if i == 'a' or 'A' or 'e' or 'E' or 'i' or 'I' or 'o' or 'O' or 'u' or 'U':
            pass
        l[i] = string[i]

    for i in l:
        print(i, sep="", end="")
main()
