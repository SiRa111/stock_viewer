def main():
    print("Amount Due : 50")
    total = int(0)
    while total != 50:
        cent = int(input("Insert Coin : "))
        total = total + cent
        print("Amount Due : ", 50 - total)



main()
