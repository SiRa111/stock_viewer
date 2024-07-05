def main(n):
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

  while True:
    try:
      dish = input("Item: ").title()
      if dish in menu:
        cost = menu[dish]
        total = n
        total = total + cost
        print(f"${total}")
        print("\n")
        main(total)
        break
      else:
        continue

    except (EOFError, ValueError):
      print("")
      return True

main(0)
