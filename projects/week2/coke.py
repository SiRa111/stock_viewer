print("Amount Due : 50")
total = 0

while total >= 50:
    cent = int(input("Insert coin : "))

    if cent == 25 or cent == 10 or cent == 5:
        total = cent + total
        due = 50 - total
        print("Amount Due : ", due)
    else :
       pass

change = total - 50
print("Change owed : ")
