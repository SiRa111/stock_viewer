def main():
    str = input("Input: ")
    print(shorten(str))

def shorten(word):
    l = []
    for i in range(len(word)):
        l.append(word[i])

    for i in l:
        if i in "aeiouAEIOU.,!@:":
            l.remove(i)

    for i in l:
        if i in "aeiouAEIOU.,!@:" :
            l.remove(i)
    final = ""
    for i in l:
        final = final + i

    return final

if __name__ == "__main__":
    main()
