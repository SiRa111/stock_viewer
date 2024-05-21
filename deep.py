ans = input("What is Answer to the Great Question of Life, the Universe, and Everything ? ")
ans1 = ans.strip().lower()
match ans1:
    case "42" | "forty-two" | "forty two"  :
        print("Yes")
    case _ :
        print("No")
