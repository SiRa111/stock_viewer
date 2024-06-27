def main():
    x = int(input("Enter first number : "))
    z = int(input("Enter second number : "))
    y = input("Enter the operator : ")
    result = operate(x,y,z)
    result = "{:.1f}".format(result)
    result = float(result)
    print(result)

def operate(a,b,c):
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



