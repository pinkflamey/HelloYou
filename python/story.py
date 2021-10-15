from getText import *


# Story sections
# ----------------------------

def t1():
    print(getText("txts/" + "t1.txt"))
    input()
    q1()

def t2():
    print(getText("txts/" + "t2" + ".txt"))
    input()
    q2()

def t2():
    print(getText("txts/" + "t2" + ".txt"))
    input()
    q2()

def t2():
    print(getText("txts/" + "t2" + ".txt"))
    input()
    q2()

def t2():
    print(getText("txts/" + "t2" + ".txt"))
    input()
    q2()

def t2():
    print(getText("txts/" + "t2" + ".txt"))
    input()
    q2()



# Questions
# ----------------------------

def q1():
    print(getText("txts/" + "q1" + ".txt"))
    a = input("Antwoord: ")
    if a == "a" or a == "A":
        t2()
    elif a == "b" or a == "B":
        t3()
    elif a == "c" or a == "C":
        t4()
    else:
        print("Voer A, B of C in.")

def q2():
    print(getText("txts/" + "q2" + ".txt"))
    a = input("Antwoord: ")
    if a == "a" or a == "A":
        t5()
    elif a == "b" or a == "B":
        t6()
    else:
        print("Voer A of B in.")