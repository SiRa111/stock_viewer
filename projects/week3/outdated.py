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
    index = valid_month(m)
    index = int(index)
    final[1] = index + 1
  else:
    final[1] = m

  for i in final:
    print(i, end="-")

  d = int(d)
  if 1 <= d <= 9:
    print(f"{d:02}, end=''")
  else:
    print(d, end='')


main()
