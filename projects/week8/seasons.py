from datetime import date
import sys
import inflect

p = inflect.engine()

def get_minutes_since_birth(birth_date):
    today = date.today()
    if birth_date > today:
        sys.exit("You can't be born in the future!")
    days_difference = (today - birth_date).days
    return days_difference * 24 * 60

def minutes_to_words(minutes):
    return p.number_to_words(minutes, andword="").capitalize()

def main():
    birth_input = input("When were you born? (YYYY-MM-DD): ")
    try:
        year, month, day = map(int, birth_input.split("-"))
        birth_date = date(year, month, day)
        minutes_lived = get_minutes_since_birth(birth_date)
        minutes_in_words = minutes_to_words(minutes_lived)
        print(f"{minutes_in_words} minutes")
    except (ValueError, TypeError):
        sys.exit("Please use YYYY-MM-DD format for your birthday")

if __name__ == "__main__":
    main()
