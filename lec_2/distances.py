distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    for name in distances.keys():
        print(f"{name} is the key -->{distances[name]} is the value")
        #this loop iterates over the KEYS of the dictionary
    print(f"{'_'}"*30)
    print("\n")

    for distance in distances.values():
        print(f"{distance} AU id {convert(distance)} in meteres")

def convert(au):
    return au * 149597870700
main()
