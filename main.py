# Number Guesser Program

# Imports 
import random
import time
import sys

# Greeting 
time.sleep(1)
print("Hello, Welcome to The Number Guesser Have fun (: )")

while True:  

    # User Input and Validation 
    try:
        time.sleep(1)
        range_Of_Number = int(input("Enter the Range of Numbers you would like the number to be chosen from: "))

    except ValueError:
        time.sleep(1)
        print("Error Restarting Program.....")
        time.sleep(0.5)
        continue

    # Generate the Number
    if range_Of_Number >= 1:
    
        time.sleep(1)
        print(f"You Chose to generate from a pool of {range_Of_Number} number's")
        number = random.randint(1, range_Of_Number)
    else:
        time.sleep(0.5)
        print("Invalid Input, Please Try Again")
        time.sleep(0.5)
        continue
    
    attempts = 0

    # Asking How Many Chances they Want
    print("These are the Options You Have (1, 2, 3, 4) \nPlease Select the Number Correspoding to your choice")
    time.sleep(0.5)
    print("1. (EASY) 20 Tries")
    time.sleep(0.5)
    print("2. (Normal) 10 Tries")
    time.sleep(0.5)
    print("3. (Medium) 7 Tries")
    time.sleep(0.5)
    print("4. (HARD) 3 Tries")
    time.sleep(1)
    try:
        time.sleep(0.5)
        option = int(input("Choose The Option Provided: "))
    except ValueError:
        time.sleep(1)
        print("Error Try Again")
        continue

    def userChosenAttempts(option1, attempts1):
        if option == option1:
            if attempts >= attempts1:
                lose1 = input(f"You Lost the number was {number}, To Exit Type (Quit) If you would like to play again type (Play):  ").lower().strip()
                if lose1 == "quit":
                    time.sleep(1)
                    print("Okay Shutting down Program...")
                    sys.exit()
                elif lose1 == "play":
                    time.sleep(1)
                    return False
                else:
                    time.sleep(1)
                    print("Invalid Input, Restarting Program....")
                    time.sleep(0.5)
                    return False
        

    # User Tries to Guess 
    while True:
        try:
            time.sleep(0.5)
            user_Guess_Number = int(input("Enter The Number You think has been Generated: "))
            attempts += 1 
        except ValueError:
            time.sleep(1)
            print("Invalid Input, Please Try Again")
            continue
        except TypeError:
            time.sleep(1)
            print("Invalid Input, Please Try Again")
            continue
        # Validition
        
        # If User Guesses it correctley 
        if user_Guess_Number == number:
            time.sleep(0.5)
            ask_To_Continue = str(input(f"You Guessed it in {attempts} attempts, Type (Quit) to Exit the Program or Type (Play) to Play Again: ")).lower().strip()
            if ask_To_Continue == "quit":
                time.sleep(1)
                print("Okay Closing Program....")
                time.sleep(0.5)
                sys.exit()
            elif ask_To_Continue == "play":
                time.sleep(1)
                print("Okay Restarting Program....")
                time.sleep(0.5)
                break

        # Lose 

        # If User Chooses 1 for Option
        userChosenAttempts(1, 20)
        # If User Chooses 2 for Option
        userChosenAttempts(2, 10)
        # If User Chooses 3 for Option
        userChosenAttempts(3, 7)
        # If User Chooses 4 for Option 
        userChosenAttempts(4, 3)
    
        # If the User Guesses To Low
        if user_Guess_Number < number:
            time.sleep(0.5)
            print("Number Too Low, Try Again.")
            continue
        # If the User Guesses To High
        elif user_Guess_Number > number:
            time.sleep(0.5)
            print("Number Too High, Try Again.")
            continue
# Code Ends
