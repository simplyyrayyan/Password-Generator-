# Password Generator
# MESSAGE: Add dictionary words check function into Program

# Imports
import string
import time
import sys
import random
import secrets 
import pyperclip

# Opening the Dictionary
try:
    with open(r"C:\Users\simpl\OneDrive\Documents\DEVELOPER\Learning Projects\Python Learning Projects\words.txt", "r") as f:
        WORD_LIST = [line.strip().lower() for line in f]
except FileNotFoundError:
    print("The dictionary file was not found.")
    sys.exit()

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
# Checking Password if it contains Dictionary Words
def check_password(password):
    password_lower = password.lower()
    return any(word in password_lower for word in WORD_LIST)

    
# Variables
message1_l = "Are you sure you want to continue without using letters? (Yes/No): "
message1_n = "Are you sure you want to continue without using numbers? (Yes/No): "
message1_s = "Are you sure you want to continue without using symbols? (Yes/No): "

password_message1 = "Your Password is Strong!"
password_message2 = "Your Password is Secure!"
password_message3 = "Your Password is Okay!"
password_message4 = "Your Password is Weak!"
password_message5 = "Your Password is Very Weak! Do not use this password!"


# Greeting
time.sleep(1)
print("Hello and Welcome to the Password Generator")

while True:
    # User Input and Validation
    try:
        time.sleep(0.5)
        user_choice = int(input("How long would you like your password to be? \n (Password Might be longer than this) \n (7-99): "))
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

        preset = input("Choose one, \n 1. Easy (A-Z) \n 2. Medium (A-Z, 0-9) \n 3. Hard (A-Z, 0-9, Symbols): ").lower().strip()

        # This allows the user to input different variations of yes and will make it still work
        if preset in ["1", "Easy", "easy", "EASY", "1. Easy", "1. easy", "1. EASY"]:
            preset = "easy"
        elif preset in ["2", "Medium", "medium", "MEDIUM", "2. Medium", "2. medium", "2. MEDIUM"]:
            preset = "medium"
        elif preset in ["3", "Hard", "hard", "HARD", "3. Hard", "3. hard", "3. HARD"]:
            preset = "hard"
        
        
        # Selecting Character Pool
        if preset == "easy":
            characters += string.ascii_letters
        elif preset == "medium":
            characters += string.ascii_letters + string.digits
        elif preset == "hard":
            characters += string.ascii_letters + string.digits + string.punctuation
        
        # Validation

        # If They user puts in an invalid input for any of the options it will ask them to try again and restart the program
        if preset not in ["easy", "medium", "hard"]:
            print("Invalid Input, Please Try Again")
            time.sleep(0.5)
            continue

    except Exception as error1:
        print(f"You have error {error1}")
        time.sleep(0.5)
        print("Restarting Program.....")
        time.sleep(0.5)
        continue 

    # Generating and Printing the Password(s)
    time.sleep(0.4)
    try:
        count = int(input("How many passwords would you like to generate?: "))
        if count == 0:
            print("You Can not generate 0 passwords")
            time.sleep(0.4)
            continue
        elif count < 0:
            print("You Can not generate a negative amount of passwords")
            time.sleep(0.4)
            continue
        elif count > 100:
            print("You Can not generate more than 100 passwords")
            time.sleep(0.4)
            continue
        
    except ValueError:
        print("Error Restarting Program.....")
        time.sleep(0.5)
        continue
    
    all_passwords = []

    for i in range(count):
        password = "".join(secrets.choice(characters) for _ in range(user_choice))

        # Making sure The password has atleast one of each character type

        # Easy -> A-Z
        if preset == "easy":
            if not any(c.isalpha() for c in password):
                password += secrets.choice(string.ascii_letters)
        
        # Medium -> A-Z, 0-9
        elif preset == "medium":
            if not any(c.isalpha() for c in password):
                password += secrets.choice(string.ascii_letters)
            if not any(c.isdigit() for c in password):
                password += secrets.choice(string.digits)

        # Hard -> A-Z, 0-9, Symbols
        elif preset == "hard":
            if not any(c.isalpha() for c in password):
                password += secrets.choice(string.ascii_letters)
            if not any(c.isdigit() for c in password):
                password += secrets.choice(string.digits)
            if not any(not (c.isalnum() or c.isspace()) for c in password):
                password += secrets.choice(string.punctuation)

        # Shuffling the Password
        password = "".join(random.SystemRandom().sample(password, len(password)))
    
        # Checking if password is Weak/Okay/Strong
        password_strength = 0

        letters1 = sum(c.isalpha() for c in password)
        numbers1 = sum(c.isdigit() for c in password)
        symbols1 = sum(not (c.isalnum() or c.isspace()) for c in password)
        length = len(password)

        if length >= 8:
            password_strength += 1
        if letters1 >= 1:
            password_strength += 1
        if numbers1 >= 1:
            password_strength += 1
        if symbols1 >= 1:
            password_strength += 1
        if length >= 12:
            password_strength += 1
    
        time.sleep(0.3)
        hidden_password = str(input("***********, Your Password is Hidden Type (REVEAL) to see: ")).lower().strip()
        if hidden_password in ["reveal", "REVEAL", "Reveal", "REVEAL", "REAVEAL", "reaveal"]:
            print(f" {i + 1}. Password: {password} \n Length: {len(password)} \n Rating: {password_strength}/5")
        else:
            print("You Typed the wrong command")
            time.sleep(0.3)
            print("********")
            ask_to_continue()

        # Printing and Checking Password Strength 
        if password_strength >= 5:
            time.sleep(0.5)
            print(password_message1)# Strong Password
        elif password_strength >= 4:
            time.sleep(0.5)
            print(password_message2) # Secure Password
        elif password_strength >= 3:
            time.sleep(0.5)
            print(password_message3) # Okay Password
        elif password_strength >= 2:
            time.sleep(0.5)
            print(password_message4) # Weak Password
        elif password_strength >= 1:
            time.sleep(0.5)
            print(password_message5) # Very Weak Password
            time.sleep(0.5)
        all_passwords.append(password)

    # Asking if they wanted to Save the password(s) to a text file
    try: 
        ask_to_save = input("Would you like to save the password(s) to a text file? (Yes/No): ").lower().strip()
        if ask_to_save == "yes":
            time.sleep(0.5)
            with open("password.txt", "a") as file:
                file.write("Generated Passwords:\n")
                for i, p in enumerate(all_passwords, start=1):
                    file.write(f"{i}. {p}\n")
                file.write("\n")
            print("Password(s) saved to password.txt")
        elif ask_to_save == "no":
            time.sleep(0.5)
            print("Password(s) not saved to password.txt")
        else:
            time.sleep(0.5)
            print("Invalid Input, Password(s) not saved to password.txt")
    except ValueError:
        print("Error Restarting Program.....")
        time.sleep(0.5)
        continue

    # Asking if they wanted to copy to clipboard

    try: 
        ask_to_copy = input("Would you like to copy the password(s) to the clipboard? (Yes/No): ").lower().strip()
        if ask_to_copy == "yes":
            time.sleep(0.5)
            pyperclip.copy("\n".join(all_passwords))
            print("Password(s) copied to clipboard")
        elif ask_to_copy == "no":
            time.sleep(0.5)
            print("Password(s) not copied to clipboard")
        else:
            time.sleep(0.5)
            print("Invalid Input, Password(s) not copied to clipboard")
    except Exception as e:
        print(f"Clipboard Error: {e}")
        time.sleep(0.5)
        print("Restarting Program.....")
        time.sleep(0.5)
        continue

    ask_to_continue()

# Code Ends 
