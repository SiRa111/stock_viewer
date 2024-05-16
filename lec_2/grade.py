score = int(input("Enter your score : "))

def grade():
    if 90 <= score <= 100:
        return "Grade A "
    elif score < 90:
        return "Grade B"
    elif score < 80:
        return "Grade C"
    elif score < 70:
        return "Grade D"
    else:
        return "Grade F"

a = grade()
print(a)
