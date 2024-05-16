score = int(input("Enter your score : "))

def grade():
    if score <= 100 and score >= 90:
        return "Grade A "
    elif score < 90 and score >= 80:
        return "Grade B"
    elif score < 80 and score >= 70:
        return "Grade C"
    elif score < 70 and score >= 60:
        return "Grade D"
    else:
        return "Grade F"

a = grade()
print(a)
