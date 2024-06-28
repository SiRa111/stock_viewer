def main():
    print("Amount Due : 50")
    total = 50
    while total != 0:
        cent = int(input("Insert Coin : "))
        if cent == 25 or cent == 10 or cent == 5:
            total = total - cent
            print("Amount Due : ",  total)
        else :
            print("Amount Due : ",  total)
            pass
    

main()
