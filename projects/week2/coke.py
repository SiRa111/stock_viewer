print("Amount Due: 50")
c = int(input("Insert Coin : "))


def main(cent):
    total = int()
    while total != 50:

        if cent == 5 or cent == 10 or cent == 25:
            total = total + cent
            if total < 50 :
                print("Amount Due: ", 50 - total)

            elif total > 50:
                print("Change Owed: ", total - 50 )
                break
        elif cent != 5 or cent != 10 or cent != 25:
            print("Amount Due: ", 50 - total)
            pass
        return total

main(c)

while input():
    if input() == int():
        
        main(input())
    else:
        break

