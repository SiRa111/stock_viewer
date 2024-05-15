def get_guess():
    guess = input("Enter a guess : ")
    return guess #saves value as a string ie "50"
'guess var equals to the user value inside this scope'

#------------------------------------------------------------

def main():
    guess = get_guess()
    'guess var stores the return value of get_guess in this scope'
    if guess == 50: #comparision bw a string and an integer
        #"50" == 50 which is incorrect
        print("Correct ! ")
    else:
        print("Incorrect ! ")

main()


"""
we use guess var here inside
two diff scopes and hence it has diff meanings in both
the scopes
"""

#correction
'''
guess = int(input("Enter a guess: "))
OR
return = int(guess)
'''
