def main():
    str = input("Input: ")
    process(str)

def process(string):
    l = []
    for i in range(len(string)):
        l.append(string[i])

    for i in l:
        if i == 'a' or  i == 'e' :
            l.remove(i)
            print(l)


main()
