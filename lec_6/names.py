name = input("Whats your name? ")

file = open("names.txt", "a") #append mode
file.write(f"{name}\n")
file.close()
