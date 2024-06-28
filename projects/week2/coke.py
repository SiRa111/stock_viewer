def main():
    print("Amount Due : 50")
    total = 0
    while total != 50:
        cent = int(input("Insert Coin : "))
        if cent == 25 or cent == 10 or cent == 5 :
            total = total + cent
            due = 50 - total
            print("Amount Due : ", due)
        elif due < cent :
            change = cent - due
            print("Change owed : ", change)

        else :
            due = 50 - total
            print("Amount Due : ", due)
            pass


main()
