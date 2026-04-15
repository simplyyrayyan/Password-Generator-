# Password Generator    

# Imports
import string
import time
import sys
import random

# Functions

# Asking to Continue Function 

def ask_to_continue():
    user_input1 = input("Would you like to (Quit) or (Continue)?: ").lower().strip()
    if user_input1 == "quit":
        time.sleep(0.8)
        print("Thanks for using the Password Generator hope to see you again!")
        sys.exit()
    elif user_input1 == "continue":
        time.sleep(0.8)
        return True
    elif user_input1 == "":
        time.sleep(0.8)
        return True
    else:
        print("Invalid Input, Please Try Again.")
        return True
# Guarentee One Option Function 
def warning_for_no_nl(option, message, message1):
    if option == "no":
            time.sleep(0.5)
            print("Not using " + message1 + " in password is not Recommended as it can make your password less secure")
            time.sleep(0.5)
            ask = str(input(message)).lower().strip()
            if ask in ["yes", "y", "yeah", "yep", "sure", "YESSS", "yesssss", "yea", "ye", "yesss"]:
                pass

            if ask in ["no", "n", "nope", "nah", "NOOOO", "noooooo", "naw", "na", "noooo"]:
                time.sleep(0.5)
                print("Okay, Restarting Program.....")
                time.sleep(0.5)
                return False
                
            else:
                time.sleep(0.5)
                print("Invalid Input, Exiting Program.....")
                time.sleep(0.5)
                sys.exit()


# Variables
message_l = "Would you like to use letters in your password? (Yes/No): "
message_n = "Would you like to use numbers in your password? (Yes/No): "
message_s = "Would you like to use symbols in your password? (Yes/No): "

message1_l = "Are you sure you want to continue without using letters? (Yes/No): "
message1_n = "Are you sure you want to continue without using numbers? (Yes/No): "
message1_s = "Are you sure you want to continue without using symbols? (Yes/No): "

# Greeting
time.sleep(1)
print("Hello and Welcome to the Password Generator")

while True:
    # User Input and Validation
    try:
        time.sleep(0.5)
        user_choice = int(input("How long would you like your password to be?: "))
        if user_choice >= 100 or user_choice <= 6:
            print("Password must be less than 100 characters long. \nPassword must be more than 6 characters long")
            time.sleep(0.5)
            continue

    except Exception as error:
        print(f"You have error {error}")
        time.sleep(0.5)
        print("Restarting Program.....")
        time.sleep(0.5)
        continue

    try: 
        characters = ""

        # Ask If they want to use letters
        letters = str(input(message_l)).lower().strip()
       
        # Ask If they want to use numbers
        numbers = str(input(message_n)).lower().strip()

        # Ask If they want to use symbols
        symbols = str(input(message_s)).lower().strip()

        # Normalize User Input

        # This allows the user to input different variations of yes and will make it still work
        if letters in ["yes", "y", "yeah", "yep", "sure", "YESSS", "yesssss", "yea", "ye", "yesss"]:
            letters = "yes"
        if numbers in ["yes", "y", "yeah", "yep", "sure", "YESSS", "yesssss", "yea", "ye", "yesss"]:
            numbers = "yes"
        if symbols in ["yes", "y", "yeah", "yep", "sure", "YESSS", "yesssss", "yea", "ye", "yesss"]:
            symbols = "yes"
        # This allows the user to input different variations of no and will make it still work
        if letters in ["no", "n", "nope", "nah", "NOOOO", "noooooo", "naw", "na", "noooo"]:
            letters = "no"
        if numbers in ["no", "n", "nope", "nah", "NOOOO", "noooooo", "naw", "na", "noooo"]:
            numbers = "no"    
        if symbols in ["no", "n", "nope", "nah", "NOOOO", "noooooo", "naw", "na", "noooo"]:
            symbols = "no"
        
        # Selecting Character Pool
        if letters == "yes":
            characters += string.ascii_letters
        if numbers == "yes":
            characters += string.digits
        if symbols == "yes":
            characters += string.punctuation
        
        # Validation

        # If They user puts in an invalid input for any of the options it will ask them to try again and restart the program
        if letters not in ["yes", "no"] or numbers not in ["yes", "no"] or symbols not in ["yes", "no"]:
            print("Invalid Input, Please Try Again")
            time.sleep(0.5)
            continue

        # If User Puts in no for letters
        if warning_for_no_nl(letters, message1_l, "letters") == False:
            continue
        # If User Puts in no for numbers
        if warning_for_no_nl(numbers, message1_n, "numbers") == False:
            continue
        # If User Puts in no for symbols
        if warning_for_no_nl(symbols, message1_s, "symbols") == False:
            continue
        
        # If the user chooses no for all options it will ask them to choose at least one option and restart the program
        if letters == "no" and numbers == "no" and symbols == "no":
            print("You have to choose at least one of the options to generate a password")
            print("Restarting Program.....")
            time.sleep(0.5)
            continue

    except Exception as error1:
        print(f"You have error {error1}")
        time.sleep(0.5)
        print("Restarting Program.....")
        time.sleep(0.5)
        continue 


    # Generating the Password
    password = "".join(random.choice(characters) for _ in range(user_choice))
    print(f" Your Password is: {password}")
    print(f"The Length of your password is: {len(password)}")
    time.sleep(1)
    ask_to_continue()
# Code Ends
