def main():
    str = input("Input: ")
    process(str)

def process(string):
    l = []
    for i in range(len(string)):
        l.append(string[i])

    for i in l:
        if i == 'a' or  i == 'e' or i == "o" or i == "u" or i == "i" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            l.remove(i)

    for i in l:
        print(i, end='')
    print('\n')

main()
