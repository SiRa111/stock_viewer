def main():
    str = input("Input: ")
    process(str)

def shorten(word):
    l = []
    for i in range(len(word)):
        l.append(word[i])

    for i in l:
        if i == 'a' or  i == 'e' or i == "o" or i == "u" or i == "i" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            l.remove(i)

    for i in l:
        if i == 'a' or  i == 'e' or i == "o" or i == "u" or i == "i" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            l.remove(i)
    final = ""
    for i in l:
        final = final + i

    return final

if __name__ == "__main__":
    main()
