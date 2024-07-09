def main():
    str = input("Input: ")
    a= shorten(str)
    for _ in a :
        print(_, end="")
    print("\n")

def shorten(word):
    l = []
    for i in range(len(word)):
        l.append(word[i])

    for i in l:
        while (
            i == "a"
            or i == "e"
            or i == "o"
            or i == "u"
            or i == "i"
            or i == "A"
            or i == "E"
            or i == "I"
            or i == "O"
            or i == "U"
            or i.isnumeric()
            or i == ","
            or i == "."
            or i == "?"
            or i == ":"
            or i == ";"
        ):
            l.remove(i)
            break
    for i in l:
        while (
            i == "a"
            or i == "e"
            or i == "o"
            or i == "u"
            or i == "i"
            or i == "A"
            or i == "E"
            or i == "I"
            or i == "O"
            or i == "U"
            or i.isnumeric()
            or i == ","
            or i == "."
            or i == "?"
            or i == ":"
            or i == ";"
        ):
            l.remove(i)
            break

    return l


if __name__ == "__main__":
    main()

