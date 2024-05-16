score = int(input("Enter your score : "))

def grade():
    if 90 >= score and score <= 100:
        return "Grade A "
    elif 80 >= score and score < 90:
        return "Grade B"
    elif 70 >= score and score < 80:
        return "Grade C"
    elif 60 >= score and score < 70:
        return "Grade D"
    else:
        return "Grade F"

a = grade()
print(a)
