def main():
  date = input()
  month,day,year = date.split("/"," ",)
  valid_month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
  ]
  if 1 <= date <= 31:
    if month.isalpha():
      if month in valid_month:
        convert(month,day,year)
      else:
        main()
    elif month.isnumeric():
      month = int(month)
      if 1 <= month <= 12:
        convert(month,day,year)
      else:
        main()

def convert(m,d,y):
  final = []
  y = int(y)
  final[0] = y
  if m.isalpha():
    final[1] = valid_month(m)




main()
