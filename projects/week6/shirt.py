import sys
from PIL import Image
from PIL import ImageOps

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        try:
            a1,b1 = sys.argv[1].split('.')
            a2,b2 = sys.argv[2].split('.')
            if b1 == b2 == 'jpg' "or 'jpeg' or 'png'":
                fit(sys.argv[1], sys.argv[2])
            elif b1 != b2:
                print("Input and output have different extensions")
                sys.argv[1]
        except:
            print("Invalid input")
            sys.exit(1)


def fit(before, after):
    with Image.open("shirt.png") as shirt:
        width = shirt.width
        height = shirt.height
        ImageOps.fit(image= before, size=(width,shirt))
        print(width)




if __name__ == "__main__":
    main()
