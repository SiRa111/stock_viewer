ans = input("What is Answer to the Great Question of Life, the Universe, and Everything ? ")
ans1 = ans.strip().lowercase()
match ans:
    case "42" | "forty-two" | "forty two" | "Forty Two" | "Forty-two" :
        print("Yes")
    case _ :
        print("No")
