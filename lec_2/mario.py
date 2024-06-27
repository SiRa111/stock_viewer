def main():
    print_column(3)
    print_row(4)

def print_column(height):
    print("#\n" * height, end="")
    # /n prints them in new line
    # end reduces the last space of \n
    '''
    alternate to:
    for i in range(height):
        print("#")
    '''
def print_row(width):
        print("?" * width, end="\n")

main()
