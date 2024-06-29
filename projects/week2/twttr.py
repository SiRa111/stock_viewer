def main():
    str = input("Input: ")
    process(str)

def process(string):
    l = [' ']
    for i in range(len(string)):
        l[i] = string[i]
        print(l)

main()
