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
        a1,b1 = sys.argv[1].split('.')
        a2,b2 = sys.argv[2].split('.')
        if b1 == b2 == ('jpg' or 'jpeg' or 'png'):
            





if __name__ == "__main__":
    main()
