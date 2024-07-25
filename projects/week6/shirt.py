import sys
from PIL import Image

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        sys.argv[1] = input_img
        sys.argv[2] = output_img
        if input_img and output_img.




if __name__ == "__main__":
    main()
