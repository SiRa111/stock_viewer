def main():
  date = input()
  if "/" in date:
    month,day,year = date.split("/")
  elif " " in date:
    month,day1,year = date.split(" ")
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
  if ',' in day1:

  day = int(day)
  if 1 <= day <= 31:
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
  else:
    main()

def convert(m,d,y):
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

  y = int(y)
  try:
    if m.isalpha():
      for _ in valid_month:
        if _ == m:
          index = valid_month.index(m)
          index = int(index)
          index = index + 1
          break
  except AttributeError:
    index = m
    pass

  print(y, end="-")

  if 1 <= index <= 9:
    print(f"{index:02}", end='-')
  else:
    print(index, end='-')

  if 1 <= d <= 9:
    print(f"{d:02}", end='\n')
  else:
    print(d, end='\n')

main()
