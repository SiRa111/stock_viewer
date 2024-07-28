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
            if b1 == b2 and b1 in ['jpg','jpeg','png']:
                try:
                    fit(sys.argv[1], sys.argv[2])
                except Exception as e:
                    print(f"error raised {e} E1")
                    sys.exit(1)
            elif b1 != b2:
                print("Input and output have different extensions")
                sys.exit(1)
        except Exception as e:
            print(f"Invalid input, {e} E2")
            sys.exit(1)


def fit(a,b):
    with Image.open("shirt.png") as shirt:
        width = shirt.width
        height = shirt.height
        with Image.open(f"{sys.argv[1]}") as before:
            ImageOps.fit(image= before, size=(width,height))
            before.paste( shirt)
            before.save("after.jpg")
            before.show()
            
        print("success")


if __name__ == "__main__":
    main()
