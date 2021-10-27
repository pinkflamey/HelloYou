from random import uniform
from time import sleep
# Slow printing function- prints 1 character at a time
def slowPrint(text, numbermin, numbermax):
    for char in text: # For every character (char) in the string (line)
        t = uniform(numbermin, numbermax)
        print(char, end="", flush="True") # Print the character, end on nothing to ensure no spaces between characters
        sleep(t) # Sleep for t amount of seconds