g = input("Greeting : ")
g1 = g.strip().lower()
match g1 :
    case g1.startswith("hello") :
        print("$0")
    case g1.startswith("h"):
        print("$20")
    case _ :
        print("$100")

