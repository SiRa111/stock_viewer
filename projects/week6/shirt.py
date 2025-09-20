import sys
import os
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Get extensions safely
    _, ext1 = os.path.splitext(input_file)
    _, ext2 = os.path.splitext(output_file)

    ext1 = ext1.lower()
    ext2 = ext2.lower()

    valid_exts = [".jpg", ".jpeg", ".png"]

    if ext1 not in valid_exts:
        sys.exit("Invalid input")
    if ext2 not in valid_exts:
        sys.exit("Invalid output")
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")

    try:
        fit(input_file, output_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")


def fit(input_file, output_file):
    # Open shirt
    shirt = Image.open("shirt.png")
    shirt_size = shirt.size

    # Open input photo
    photo = Image.open(input_file)

    # Resize and crop to match shirt size
    photo = ImageOps.fit(photo, shirt_size)

    # Overlay shirt with transparency mask
    photo.paste(shirt, shirt)

    # Convert to RGB if saving as JPG
    if output_file.lower().endswith((".jpg", ".jpeg")):
        photo = photo.convert("RGB")

    # Save result
    photo.save(output_file)


if __name__ == "__main__":
    main()
