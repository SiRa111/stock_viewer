def main():
    print("Amount Due : 50")
    total = 0
    while total != 50:
        cent = int(input("Insert Coin : "))
        total = total + cent
        if cent == 5 or cent == 10 or cent == 25:
            if total < 50 :
                print("Amount Due : ", 50 - total)
            elif total > 50:
                print("Change Owed : ", total - 50 )
                break
            else :
                print("Amount Due : 0")
                break
        else:
            print("Amount Due : ", 50 - total)
            pass

main()
