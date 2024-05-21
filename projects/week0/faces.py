def convert(og_string):
    alt_string1 = og_string.replace(":)","🙂",12)
    alt_string2 = alt_string1.replace(":(","🙁",12)
    return alt_string2

def main():
    og = input("Enter something : ")
    a = convert(og)
    print(a)

main()

