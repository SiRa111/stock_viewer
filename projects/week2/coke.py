print("Amount Due : 50")
total = 0
if total <= 50 :
    while total != 50:
        cent = int(input("Insert coin : "))
        due = 50 - total
        if cent == 25 or cent == 10 or cent == 5:
            total = cent + total
            print("Amount Due : ", due)

        else :
            pass
elif total > 50 :
    change = total - 50
    print("Change owed : ")
