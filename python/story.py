from getText import *
from slowPrint import *


# Story sections
# ----------------------------

def t1():
    print("\n" + "Sectie 1".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t1.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    q1()





# Questions
# ----------------------------

def q1():
    print("\n" + "Vraag 1".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "q1" + ".txt") + "\n\n", 0.01, 0.08)

    slowPrint("A. Ja".center(100), 0.01, 0.02)
    slowPrint("B. Nee".center(100), 0.01, 0.02)
    slowPrint("C. Ik ga niet".center(100), 0.01, 0.02)

    a = ""
    
    while a == "":
        a = input("\n\nAntwoord:")
        if a == "a" or a == "A":
            t2()
        elif a == "b" or a == "B":
            t3()
        elif a == "c" or a == "C":
            t4()
        else:
            print("Voer A, B of C in.")
        print("Voer A, B of C in.")

input()