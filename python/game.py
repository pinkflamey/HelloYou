import os
from sys import platform, stdout
from time import sleep


#-------------------------------------------
# Logic Functions
from getText import *
from slowPrint import *
from printLines import *
from clearScreen import *
from changeScreenSize import *


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


#-------------------------------------------
# Story functions

from story import *


#-------------------------------------------
# Start script

changeScreenSize(66, 38)

print(getText("txtimgs/tree.txt"))
print(getText("txtimgs/helloyou.txt"))
input("Press [ENTER] to start...")

sleep(1)

changeScreenSize(50, 4)

title = "Verhaal van een nieuwkomer".center(50, "-")
print("\n"+title)
loading = "[»-(¯`·.·´¯)->...LOADING...<-(¯`·.·´¯)-«]".center(50)
slowPrint(loading, 0.01, 0.13)
slowPrint("...", 0.8, 0.8)

changeScreenSize(100, 25)


#-------------------------------------------
# Explanation

print('')
print("Uitleg".center(100, "-"))
sleep(0.5)
print('\n\n')
print('- Het spel bestaat uit stukjes verhaal ("secties") en vragen;'.center(100))
sleep(1.5)
print('- Bij elke vraag kun je A, B en soms C antwoorden;'.center(100))
sleep(1.5)
print('- De keuzes die je maakt beïnvloeden hoe het verhaal verloopt. Maak je keuzes aandachtig.'.center(100))
sleep(2.5)

x = input('\n\n\n\n\n\nOm het spel te starten, druk op [ENTER]. Om de credits te bekijken, typ "credits".\n')

clearScreen()

if x.lower() == "credits":

    print('\n')
    print('Credits'.center(100, "-"))
    print('\n\nDit keuzeverhaal spel is gemaakt door Mavis de Ridder uit klas SD1C van het Mediacollege Amsterdam, als eind-beroepsopdracht voor periode 1, jaar 1.')
    print('\n\nDe GitHub link voor dit project is: [https://github.com/pinkflamey/HelloYou]')

    input('Druk op [ENTER] om het spel te starten...')
    clearScreen()
    t1()
    
else:

    clearScreen()
    t1()