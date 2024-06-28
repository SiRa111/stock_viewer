def main():
    cent = int(input("Amount Due : 50\nInsert Coin : "))
    due(cent)

def due(value):
    total= 50

    while value == 25 or value == 10 or value == 5 :
        total = total - value
        print("Amount Due : ",total)
        continue


main()
