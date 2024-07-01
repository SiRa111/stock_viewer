print("Amount Due: 50")
c = int(input("Insert Coin : "))


def main(cent):
    total = int()
    while total != 50:
        if cent == 5 or cent == 10 or cent == 25:
            total = total + cent
            if total < 50 :
                print(f"Amount Due: {50 - total}\n" )

            elif total > 50:
                print(f"Change Owed: {total - 50}\n" )
                break
        elif cent != 5 or cent != 10 or cent != 25:
            print(f"Amount Due: {50 - total}\n")
            pass

main(c)










