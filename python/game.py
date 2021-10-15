import os
from sys import platform, stdout
from time import sleep




#-------------------------------------------
# Logic Functions
from getText import *
from slowPrint import *
from printLines import *

platform = platform
def clearScreen(): # Clears the screen for Windows, Mac and Linux
    if platform == "win32":
        os.system('cls')
    else:
        os.system('clear')

# "Waiting" animation with dots. Allows control over the number of dots in each cycle, the amount of cycles, and the time between each dot.
def waitingDots(num_of_dots, num_of_loops, dot_speed, char):
    l = 0
    str = char * num_of_dots # All dots in 1 string
    while l < num_of_loops:
        for char in str: # Print each character in str with dot_speed amount of time in between
            print(char, end="", flush="True")
            sleep(dot_speed)
        for char in str: # Go back one space and clear it for each dot
            stdout.write("\b" * num_of_dots)
            stdout.write(" " * num_of_dots)
            stdout.write("\b" * num_of_dots)
        l = l + 1

def changeScreenSize(col, lin):
    if platform == "win32":
        os.system("mode con: cols="+str(col)+" lines="+str(lin))
    else:
        os.system("resize -s "+str(lin)+" "+str(col))



#-------------------------------------------
# Story functions
from story import *



#-------------------------------------------
# Start script

changeScreenSize(66, 38)

print(getText("txtimgs/tree.txt"))
print(getText("txtimgs/helloyou.txt"))
print("\nPress [ENTER] to start...", end="")

input()

changeScreenSize(50, 2)

print("Loading...".center(50, "-"))
waitingDots(50, 2, 0.02, "/")

changeScreenSize(100, 25)

print("-", end="")
print("Verhaal van een nieuwkomer".center(98, "="), end="")
print("-")

slowPrint("")

input()