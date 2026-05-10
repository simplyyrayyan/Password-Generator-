import time
import sys

def slow_print(text, speed=0.08):
    """
    Prints text slowly to the terminal.
    speed: Time in seconds between characters.
    """
    for char in text:
        # sys.stdout.write ensures the buffer updates properly
        sys.stdout.write(char)
        sys.stdout.flush() 
        time.sleep(speed)
    print() # Adds a newline at the end


import time
import sys

def slow_input(prompt, speed=0.05):
    # 1. Print the prompt slowly
    for char in prompt:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    
    # 2. Return the actual input
    return input()
