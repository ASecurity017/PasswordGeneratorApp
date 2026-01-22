
# import enum module
from enum import Enum

# import secrets module
import secrets

# import string module
import string
# import datetime module
import datetime


# Enum class to define Password Strength Levels
class passwordStrengthLevel(Enum):

    INIT : int = 0
    WEAK: int = 1
    STRONG: int = 2
    VERYSTRONG: int = 3

def main():


 """ Function to determine a given password's strength level"""
def isPasswordStrong(password, currentStrengthLevel: passwordStrengthLevel) -> passwordStrengthLevel:


    StrengthLevelScore = 0

    displayStrengthLevel = ""

    #If the password is 8 characters or more its strong
    if len(password) >= 8:

        # Add 1 point to the strength level score
        StrengthLevelScore +=1

    else:
        # Take away 1 point to the strength level score if it is less than 8 characters
        StrengthLevelScore -=1


    # For each character in the password
    for char in password:
        # If the characters are a mix of uppercase and lowercase characters
        if char.isupper() or char.islower():
            # Add 1 point to the strength level score
            StrengthLevelScore += 1


    # For each character in the password
    for char in password:
        if char.isdigit():
            # Add 1 point to the strength level score
            StrengthLevelScore += 1
    # For each character in the password
    for char in password:
        # If password contains a special character - @!%?
        if char.isalnum():
            # Add 1 point to the strength level score
            StrengthLevelScore += 1

    # If the strength level is 5 or less
    if StrengthLevelScore <= 20:
        # Set the current Strength level to Weak
        currentStrengthLevel = passwordStrengthLevel.WEAK

    # If the strength level is between 20 and 25
    elif  StrengthLevelScore > 20 and StrengthLevelScore <= 25 :
        # Set the current Strength level to Strong
        currentStrengthLevel = passwordStrengthLevel.STRONG

    # If the strength level is above 25
    elif StrengthLevelScore > 25:
        # Set the current Strength level to Very Strong
        currentStrengthLevel = passwordStrengthLevel.VERYSTRONG


    # If the currentStrength level is declared as WEAK

    if currentStrengthLevel == passwordStrengthLevel.WEAK:

        # Print out point system and password's strength level to the user

        print("##############################################")
        print("Score Level Range: ")
        print("WEAK = (20 Points Or Less)")
        print("STRONG = (20 - 25 Points)")
        print("VERY STRONG = (25+ Points)")
        print("##############################################")
        print("Password is considered Weak")

    # If the currentStrength level is declared as STRONG

    if currentStrengthLevel == passwordStrengthLevel.STRONG:

        # Print out point system and password's strength level to the user

        print("##############################################")
        print("Score Level Range: ")
        print("WEAK = (20 Points Or Less)")
        print("STRONG = (20 - 25 Points)")
        print("VERY STRONG = (25+ Points)")
        print("##############################################")
        print("Password is considered Strong")

    # If the currentStrength level is declared as VERY STRONG

    if currentStrengthLevel == passwordStrengthLevel.VERYSTRONG:

        # Print out point system and password's strength level to the user

        print("##############################################")
        print("Score Level Range: ")
        print("WEAK = (20 Points Or Less)")
        print("STRONG = (20 - 25 Points)")
        print("VERY STRONG = (25+ Points)")
        print("##############################################")
        print("Password is considered Very Strong")

    print("Strength Level Score: " + str(StrengthLevelScore))

    # Return current Strength Level of Newly Password Created
    return currentStrengthLevel


""" Function to generate a password of a Given Length"""

def generate_password(length: int) -> str:

    
    # storing letters, numbers and special characters
    charset = string.ascii_letters + string.digits + "!@?%"

    while True:
        # random sampling by joining the length of the password and the variables
        password = "".join(secrets.choice(charset) for i in range(length))
        # Ensures password contains a lower character, an upper character, a random character and 3 digits
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password )
            and any(c.isalnum() for c in password )
            and sum(c.isdigit() for c in password) >= 3):

            break

    # Return password

    return password



""" Function to save a password of a Given Strength Level"""
def save_password(password: str, currentStrengthLevel: passwordStrengthLevel ):

    # Call function to determine password's strength level
    passwordStrengthLevel = isPasswordStrong(password, currentStrengthLevel)

    # If the password is strong or very strong
    if (passwordStrengthLevel == passwordStrengthLevel.STRONG
            or passwordStrengthLevel == passwordStrengthLevel.VERYSTRONG):

        # Open the csv file and save the strong or very strong password with the date and time
        with open("passwordFile.csv", "a") as f:

            f.write( "\n" + "Password Saved      ||         Date and Time" + "\n")
            f.write(password + "      ||        " + str(datetime.datetime.now()))
        f.close()

        print("Password Saved Successfully")
        # output the newly created strong password
        print(f"Your New Password:  {password}")
    else:
        print("Password is too weak, Please try again")


if __name__ == '__main__':

    main()
