name = input("What is your name ?")

'''
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Bruh. Who?")
'''

match name:
    case "Harry" | "Hermione" | "Ron" :
        print("Gryffindor")
    case "Draco" :
        print("Slytherin")
    case _:  #matches with any input
        print("BRUH. Who ?")
