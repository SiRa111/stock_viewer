def main():
    fuel = input("Fraction: ")
    final = convert(fuel)
    try:
       print(gauge(final))
    except TypeError:
       print(final)


def convert(str):
  n,d = str.split('/')
  n = int(n)
  d = int(d)
  if n < d:
      s = float((n/d))
      s = round(s*100)
      return s
  elif n == d:
      s = 1
      return s
  elif n > d and d != 0:
    raise ValueError
  elif d == 0 :
    raise ZeroDivisionError


def gauge(percentage):
    if percentage > 100:
        main()
        return
    elif 99 <= percentage:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
