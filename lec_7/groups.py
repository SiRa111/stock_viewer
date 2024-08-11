import re

locations = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}

def main():
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    #\+ : we literally want +
    #\d : we want decimal digits ie 0 to 9
    #they can be 1 or 3 digits
    #it is named country code


    number = input("Number: ")

    match = re.search(pattern, number)
    if match:
        country_code = match.group("country_code")
        print(locations[country_code])
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
