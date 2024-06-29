def main():
    str = input("Input: ")
    process(str)

def process(string):
    l = []
    for i in range(len(string)):
        l.append(string[i])
        print(l)

main()
