import sys
from PIL import Image,ImageOps



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
        with Image.open(f"{sys.argv[1]}") as before:
            height = before.height
            fitted_image = ImageOps.fit(image= before, size=(width,height), bleed = 0.0, centering =(0.5, 0.5))
            fitted_image.save("after.jpg")

            fitted_image.paste( shirt)

            fitted_image.save("after.jpg")
            fitted_image.show()

        print("success")


if __name__ == "__main__":
    main()
