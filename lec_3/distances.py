distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}

def main():
    spacecraft = input("Enter a spacecraft: ")
    try:
        au = float(distances[spacecraft])
        m = convert(au)
        print(f"{m} m away")
    except KeyError:
        print(f"'{spacecraft}' is not in dictionary")
        return
    except ValueError:
        print(f"Cant convert '{distances[spacecraft]}' to a float")
        return
def convert(au):
    return au * 149597870700

main()

'''
as you write code, try to anticipate the error and except cases to handle those errors'''
