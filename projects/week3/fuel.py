def main():
    fuel = input("Fraction: ")

    n,d = fuel.split('/')
    final = run(n,d)
    if final == 1:
        print("F")
    elif final == 0:
        print("E")
    elif final > 1:
        main()
        return
    else:
        print(final,"%")

def run(a,b):
    try:
        return int(a/b)
    except ZeroDivisionError:
        main()
        return
    except ValueError:
        main()
        return

main()
