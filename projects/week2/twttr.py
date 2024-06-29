def main():
    str = input("Input: ")
    process(str)

def process(string):
    l = []
    for i in range(len(string)):

        if i == 'a'|'A'|'e'|'E'|'i'|'I'|'o'|'O'|'u'|'U':
            pass
        l[i] = string[i]

    for i in l:
        print(i, sep="", end="")
main()
