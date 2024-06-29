def main():
    print("Amount Due : 50")
    total = 0
    while total != 50:
        cent = int(input("Insert Coin : "))
        total = total + cent
        if total <= 50 :
            prod(cent)
        elif total > 50:
            change(cent)

def prod(a):
    

main()
