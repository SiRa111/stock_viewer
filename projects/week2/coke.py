def main():
    print("Amount Due : 50")
    total = int(0)
    while total != 50:
        cent = int(input("Insert Coin : "))
        if cent == 25 or cent == 10 or cent == 5:
            total = total + cent
            print("Amount Due : ", 50 - total)
        else :
            pass


main()
