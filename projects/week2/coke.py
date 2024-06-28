def main():
    print("Amount Due : 50")
    cent = int(input("Insert Coin : "))
    due(cent)

def due(value):
    total= 0
    if value == 25 or value == 10 or value == 5 :
        while total != 0:
            total = total + value
            print("Amount Due : ",50 - total)
            continue
    elif


main()
