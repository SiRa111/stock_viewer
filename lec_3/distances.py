distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}

def main():
    spacecraft = input("Enter a spacecraft: ")
    m = convert(distances[spacecraft])
    print(f"{m} m away")

def convert(au):
    return au * 149597870700

main()
