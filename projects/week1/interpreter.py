def main():
    expression = input("Enter the expression : ")
    x,y,z = expression.split(" ")


    result = operate(x,y,z)
    result = "{:.1f}".format(result)
    result = float(result)
    print(result)


def operate(a,b,c):
    a = int(a)
    c = int(c)

    match b:
        case '+':
            final = a + c
        case '-':
            final = a - c
        case '/':
            final = a / c
        case '*':
            final = a*c
    return final

main()



