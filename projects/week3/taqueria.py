def main():
    item = input("Item: ").title()
    order(item)

def order(dish):
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    total = 0
    while True:
        for dish in menu:
            print(dish)
            total = total + menu[dish]
            print(total)
        break
main()
