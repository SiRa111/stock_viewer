def main():
    print("Amount Due: 50")
    total = 0

    while total != 50:
        i = 0
        while i == 0:
            cent = int(input("Insert Coin: "))
            i += 1
        cent = int(input(""))

        if cent == 5 or cent == 10 or cent == 25:
            total = total + cent
            if total < 50 :
                print("Amount Due: ", 50 - total)

            elif total > 50:
                print("Change Owed: ", total - 50 )
                break
        else:
            print("Amount Due: ", 50 - total)
            pass

main()
