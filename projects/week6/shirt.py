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
        shirt_width, shirt_height = shirt.size

        with Image.open(f"{sys.argv[1]}") as before:

            fitted_image = ImageOps.fit(image= before, size=(shirt_width, shirt_width), method = 0, bleed = 0.0, centering =(0.5, 0.5))
            result_image = Image.new('RGBA', fitted_image.size)
            result_image.paste(fitted_image, (0, 0))

            paste_x = (result_image.width - shirt_width)
            paste_y = result_image.height - shirt_height

            result_image.paste(shirt, (paste_x, paste_y), shirt)

            if sys.argv[2].lower().endswith(('.jpg', '.jpeg')):
                result_image = result_image.convert('RGB')

            result_image.save(sys.argv[2])
            result_image.show()

        print("success")


if __name__ == "__main__":
    main()
