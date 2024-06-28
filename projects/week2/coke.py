def main():
    print("Amount Due : 50")
    total = 50
    while total != 0:
        cent = int(input("Insert Coin : "))
        if cent == 25 or cent == 10 or cent == 5 and total > cent:
            total = total - cent
            print("Amount Due : ",  total)
        elif total < cent :
            change = cent - total
            print("Change owed : ", change)
        else :
            print("Amount Due : ",  total)
            pass
    change = 50 + total
    print("Change owed : ", change)

main()
