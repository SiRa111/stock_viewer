def main():
    print_column(3)
    print_row(4)
    print_square(5)

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

def print_square(size):

     #to print row in sqaure
     for i in range(size):

          #to print each brick in row
          for j in range(size):
               print("#", end="")

          #to bring hash to the next line after col prnt
          print(end="\n")

main()
