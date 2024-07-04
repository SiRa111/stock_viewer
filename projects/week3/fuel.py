def main():
    fuel = input("Fraction: ")
    n,d = fuel.split('/')
    n = int()
    d = int()
    final = run(n,d)
    if final == 1:
        print("F")
    elif final == 0:
        print("E")
    else:
        print(final,"%")

def run(a,b):
    try:
        return int(a/b)
    except ZeroDivisonError:
        main()
        return
    except ValueError:
        main()
        return
    except a>b :
        main()
        return
main()
