# Password Generator Program

# MESSAGE: add slow printing and slow input

# Imports
import secrets, time, sys, string, pyperclip 
from slow_printing import slow_print, slow_input
# Opening the Dictionary
try:
    with open(r"C:\Users\simpl\OneDrive\Documents\DEVELOPER\Learning Projects\Python Learning Projects\words.txt", "r") as f:
        WORD_LIST = set([line.strip().lower() for line in f])
except FileNotFoundError:
    slow_print("The dictionary file was not found.")
    sys.exit()

# Functions

# Asking the user if they want to continue.
def ask_to_continue():
    try:
        user_input1 = slow_input("Would you like to (Quit) or (Continue)?: ").lower().strip()
        if user_input1 == "quit":
            slow_print("Thanks for using the Password Generator hope to see you again!")
            sys.exit()
        elif user_input1 == "continue":
            return True
        elif user_input1 == "":
            return True
        else:
            slow_print("Invalid Input, Please Try Again.")
            return True
    except ValueError:
        slow_print("Error Exiting Program.....")
        sys.exit()
# Checking Password if it contains Dictionary Words
def contains_dictionary_word(password: str): 
    
    try:
        password_lower = password.lower()
        return any(word in password_lower for word in WORD_LIST)
    except ValueError:
        slow_print("Error Exiting Program.....")
        sys.exit()
# Saving Password to a Text File Function
def save_txt_file():
    try: 
        ask_to_save = slow_input("Would you like to save the password(s) to a text file? (Yes/No): ").lower().strip()
        if ask_to_save in ["yes", "yea", "y", "ye"]:
            with open("password.txt", "a") as file:
                file.write("Generated Passwords:\n")
                for i, p in enumerate(all_passwords, start=1):
                    file.write(f"{i}. {p}\n")
                file.write("\n")
            slow_print("Password(s) saved to password.txt")
        elif ask_to_save in ["no", "n", "no"]:
            slow_print("Password(s) not saved to password.txt")
        else:
            slow_print("Invalid Input, Password(s) not saved to password.txt")
    except ValueError:
        slow_print("Error Exiting Program.....")
        sys.exit()
# Copy to Clipboard Function
def copy_to_clipboard():
    try: 
        ask_to_copy = slow_input("Would you like to copy the password(s) to the clipboard? (Yes/No): ").lower().strip()
        if ask_to_copy in ["yes", "yea", "y", "ye"]:
            pyperclip.copy("\n".join(all_passwords))
            slow_print("Password(s) copied to clipboard")
        elif ask_to_copy in ["no", "n", "no"]:
            slow_print("Password(s) not copied to clipboard")
        else:
            slow_print("Invalid Input, Password(s) not copied to clipboard")
    except Exception as e:
        slow_print(f"Clipboard ERROR: {e} ")
        slow_print("Exiting Program.....")
        sys.exit()
# Password Strength Check Function
def password_strength_check():
# Password Strength Check 
    if password_strength >= 5:
        slow_print(password_message1) # Strong Password

    elif password_strength >= 4:
        slow_print(password_message2) # Secure Password

    elif password_strength >= 3:
        slow_print(password_message3) # Okay Password

    elif password_strength >= 2:
        slow_print(password_message4) # Weak Password

    elif password_strength >= 1:
        slow_print(password_message5) # Very Weak Password
# Password Reveal Function and Printing Password
def password_reveal():
    hidden_password = str(slow_input("***********, Your Password is Hidden Type (REVEAL) to see: ")).lower().strip()
    if hidden_password in ["reveal", "REVEAL", "Reveal", "REVEAL", "REAVEAL", "reaveal"]:
        slow_print(f" {i + 1}. Password: {password} \n Length: {len(password)} \n Rating: {password_strength}/5", speed=(0.05) )
    else:
        slow_print("You Typed the wrong command")
        slow_print("********")
        ask_to_continue()
# If there is a Repeated Character
def is_repeated_chars(password: str):
    for a, b, c in zip(password, password[1:], password[2:]):
        if a == b == c:
            return True
    return False
def is_sequential_chars(password: str):
    sequences = {
    # Forward Alphabet
    "abc", "bcd", "cde", "def", "efg", "fgh", "ghi", "hij", "ijk", 
    "jkl", "klm", "lmn", "mno", "nop", "opq", "pqr", "qrs", "rst", 
    "stu", "tuv", "uvw", "vwx", "wxy", "xyz",

    # Reverse Alphabet
    "zyx", "yxw", "xwv", "wvu", "vut", "uts", "tsr", "srq", "rqp", 
    "qpo", "pon", "onm", "nml", "mlk", "lkj", "kji", "jih", "ihg", 
    "hgf", "gfe", "fed", "edc", "dcb", "cba",

    # Forward Numbers
    "012", "123", "234", "345", "456", "567", "678", "789", "890",

    # Reverse Numbers
    "210", "321", "432", "543", "654", "765", "876", "987", "098",

    }

    password_lower = password.lower()

    for seq in sequences:
        if seq in password_lower:
            return True
    return False
def is_keyboard_pattern(password: str):

    keyboard_patterns = {
        "qwerty", "asdf", "zxcv",
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm",
        "1234", "12345", "123456", "1234567", "12345678", "123456789", "1234567890",
        "qaz", "wsx", "edc", "rfv", "tgb", "yhn", "uio", "jkl", "mnb", "vxc", "zlk", 
        "1qaz", "2wsx", "3edc", "4rfv", "5tgb", "6yhn", "7ujm", "8ik,", "9oln", "0p;/", "zlk",
    }
    
    password_lower = password.lower()

    for k_pattern in keyboard_patterns:
        if k_pattern in password_lower:
            return True
    return False
def is_weak_password(password: str):
    if contains_dictionary_word(password) == True:
        return True
    if is_repeated_chars(password) == True:
        return True
    if is_sequential_chars(password) == True:
        return True
    if is_keyboard_pattern(password) == True:
        return True
    
    return False
    
    
# Variables
message1_l = "Are you sure you want to continue without using letters? (Yes/No): "
message1_n = "Are you sure you want to continue without using numbers? (Yes/No): "
message1_s = "Are you sure you want to continue without using symbols? (Yes/No): "

password_message1 = "Your Password is Strong!"
password_message2 = "Your Password is Secure!"
password_message3 = "Your Password is Okay!"
password_message4 = "Your Password is Weak!"
password_message5 = "Your Password is Very Weak! Do not use this password!"

password_length_question = "How long would you like your password to be?\n (7-99): "
error_message1 = "Password must be less than 100 characters long. \nPassword must be more than 6 characters long"
greeting = "Hello and Welcome to the Password Generator"
restart_message = "Restarting Program....."

easy_list = ["1", "Easy", "easy", "EASY", "1. Easy", "1. easy", "1. EASY", "esy", "ESY", "esY", "EsY"]
medium_list = ["2", "Medium", "medium", "MEDIUM", "2. Medium", "2. medium", "2. MEDIUM", "Medum", "MEDUM", "medum"]
hard_list = ["3", "Hard", "hard", "HARD", "3. Hard", "3. hard", "3. HARD"]

try:
    # Greeting
    slow_print(greeting)

    # Main Loop & Program
    while True:

        # Defining all_passwords
        all_passwords = []
        # User Input and Validation
        try:
            password_length = int(slow_input(password_length_question))
            if password_length >= 100 or password_length <= 6:
                slow_print(error_message1)
                continue

        except Exception as error:
            slow_print(f"You have error {error}")
            slow_print(restart_message)
            continue

        try:

            characters = ""

            preset = slow_input("Choose one, \n 1. Easy (A-Z) \n 2. Medium (A-Z, 0-9) \n 3. Hard (A-Z, 0-9, Symbols): ").lower().strip()

            # This allows the user to input different variations of yes and will make it still work
            if preset in easy_list:
                preset = "easy"
            elif preset in medium_list:
                preset = "medium"
            elif preset in hard_list:
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
                slow_print("Invalid Input, Please Try Again")
                continue

        except Exception as error1:
            slow_print(f"You have error {error1}")
            slow_print(restart_message)
            continue 

        # Get and limit password count to a valid range (1-100)
        try:
            count = int(slow_input("How many passwords would you like to generate?: "))
            if count == 0:
                slow_print("You Can not generate 0 passwords")
                continue
            elif count < 0:
                slow_print("You Can not generate a negative amount of passwords")
                continue
            elif count > 100:
                slow_print("You Can not generate more than 100 passwords")
                continue

        
        except ValueError:
            slow_print(restart_message)
            continue
    

    # Generating the Password
        for i in range(count):
            retry_counter = 0
            password_strength = 0

            while True:

                # Generating the Password
                if preset == "easy":
                    password = secrets.choice(string.ascii_letters)
                    remaining_length = password_length - 1

                elif preset == "medium":
                    password = (secrets.choice(string.ascii_letters) +
                        secrets.choice(string.digits))
                    remaining_length = password_length - 2
                    
                elif preset == "hard":
                    password = (secrets.choice(string.ascii_letters) +
                        secrets.choice(string.digits) +
                        secrets.choice(string.punctuation))
                    remaining_length = password_length - 3

                password += "".join(secrets.choice(characters) for _ in range(remaining_length))

                # Shuffling the Password
                password = "".join(secrets.SystemRandom().sample(password, len(password)))  

                # Seeing if the password has repeated characters
                if is_weak_password(password):
                    retry_counter += 1
                    if retry_counter >= 100:
                        break
                    else:
                        continue
                break

            # Checking if password has atleast one of each character type

            letters_check = sum(c.isalpha() for c in password)
            numbers_check = sum(c.isdigit() for c in password)
            symbols_check = sum(not (c.isalnum() or c.isspace()) for c in password)
            length_check = len(password)

            if length_check >= 10:
                password_strength += 1
            if letters_check >= 1:
                password_strength += 1
            if numbers_check >= 1:
                password_strength += 1
            if symbols_check >= 1:
                password_strength += 1
            if length_check >= 14:
                password_strength += 1
        
            # Adding the Passwords to all_paswords list
            all_passwords.append(password)

            # Reveal Password Option
            password_reveal()

            # Printing and Checking Password Strength 
            password_strength_check()

        # Asking if they wanted to Save the password(s) to a text file
        save_txt_file()

        # Asking if they wanted to copy to clipboard
        copy_to_clipboard()

        # Asking to Continue
        ask_to_continue()

# If user presses Ctrl + C/c then program will exit anywhere
except KeyboardInterrupt:
    slow_print("Thanks for using Password Generator")
    sys.exit()

# Code Ends Here
