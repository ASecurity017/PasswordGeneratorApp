
from passwordGenerator import generate_password
from passwordGenerator import save_password
from passwordGenerator import passwordStrengthLevel

def menuFunction():


    while True:

        # Prints out Menu Description for User

        print("############################")
        print("Menu for User:")
        print("1. Generate Strong Password")
        print("2. Create My Own Password")
        print("3. Quit")
        print("############################")

        print("Select an option:")
        userInput = int(input(""))

        match userInput:
            case 1:  # Take user input for password length
                    pass_length = int(input("Enter the length of the password: "))

                    # If the user enter a length less than 14
                    if pass_length < 16:

                        # Keep looping until the user enters a length of 14 or greater to ensure strong security
                        while pass_length < 16:
                            # Prompt the user to re-enter their password length
                            pass_length = int(input("Please Enter A Length Of 16 Characters Or More Characters: "))

                    # Call the function to generate the password and store it in a variable
                    password = generate_password(pass_length)
                    # Save password to CSV file if it is strong or very strong
                    save_password(password, passwordStrengthLevel.INIT)

            # User Enters Option 2 To Create Their Own Password
            case 2:
                userInput = input("Enter your own strong password: ")
                # Store password inputted by the user
                password = userInput

                # Save password to CSV file if it is strong or very strong
                save_password(password, passwordStrengthLevel.INIT)


            # User Enters Option 3 to Quit Application
            case 3:
                print("Program has been exited by the user")
                # Break Out Of Loop To Quit The Program
                break


# Call Menu function
menuFunction()