def main():
    print("Amount Due : 50")
    total = 0
    while total != 50:
        cent = int(input("Insert Coin : "))
        if cent == 25 or cent == 10 or cent == 5 :
            total = total + cent
            print("Amount Due : ", 50 -  total)
            if total < cent :
                change = cent + total
                print("Change owed : ", change)
            elif
        else :
            print("Amount Due : ", 50 - total)
            pass
    change = 50 + total
    print("Change owed : ", change)

main()
