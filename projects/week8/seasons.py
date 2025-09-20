from datetime import date, datetime
import sys
from num2words import num2words

def main():
    dob_input = input("Date of birth (YYYY-MM-DD): ").strip()
    try:
        dob = datetime.strptime(dob_input, "%Y-%m-%d").date()
    except ValueError:
        sys.exit(1)

    minutes = minutes_since_birth(dob)
    minutes_words = number_to_words(minutes)
    print(minutes_words)

def minutes_since_birth(birth_date):
    today = date.today()
    delta_days = (today - birth_date).days
    return delta_days * 24 * 60

def number_to_words(n):
    words = num2words(n, to='cardinal')
    words = words[0].upper() + words[1:]
    return f"{words} minutes"

if __name__ == "__main__":
    main()
