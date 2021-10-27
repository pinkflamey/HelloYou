from getText import *
from slowPrint import *
from clearScreen import *
from changeScreenSize import *


# Story sections
# ----------------------------

def t1():
    changeScreenSize(100, 25)

    print("\n" + "Sectie 1".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t1.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    q1()

def t2():
    print("\n" + "Sectie 2".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t2.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    q2()

def t3():
    print("\n" + "Sectie 3".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t3.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    q3()

def t4():
    print("\n" + "Sectie 4".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t4.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    q10()

def t5():
    print("\n" + "Sectie 5".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t5.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    q5()

def t6():
    print("\n" + "Sectie 6".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t6.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    q6()

def t7():
    print("\n" + "Sectie 7".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t7.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    q7()

# There is no section 8! I don't feel like renaming every section. (23/10/21)

def t9():
    print("\n" + "Sectie 9".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t9.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    q9()

def t10():
    print("\n" + "Sectie 10".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t10.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    q10()

def t11():
    print("\n" + "Sectie 11".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t11.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    q10()

def t12():
    print("\n" + "Sectie 12".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t12.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    q12()

def t13():
    print("\n" + "Sectie 13".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t13.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    q13()

def t14():
    print("\n" + "Sectie 14".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t14.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    e2()

def t15():
    print("\n" + "Sectie 15".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t15.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    q15()

def t16():
    print("\n" + "Sectie 16".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t16.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    e1()

def t17():
    print("\n" + "Sectie 17".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t17.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    e2()

def t18():
    print("\n" + "Sectie 18".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t18.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    q18()

def t19():
    print("\n" + "Sectie 19".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t19.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    e3()

def t20():
    print("\n" + "Sectie 20".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t20.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    b1()

def t21():
    print("\n" + "Sectie 21".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t21.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    e4()

def t22():
    print("\n" + "Sectie 22".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t22.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    q22()

def t23():
    print("\n" + "Sectie 23".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t23.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    e5()

def t24():
    print("\n" + "Sectie 24".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "t24.txt") + "\n", 0.01, 0.08)
    input("\n[Druk op enter om door te gaan]")
    e6()


# Questions
# ----------------------------

def q1():
    print("\n" + "Vraag 1".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "q1" + ".txt") + "\n\n", 0.01, 0.08)

    slowPrint("A. Ja".center(100), 0.01, 0.02)
    slowPrint("B. Nee".center(100), 0.01, 0.02)
    slowPrint("C. Ik ga niet".center(100), 0.01, 0.02)

    a = ""
    
    while a.lower() != "a" or a.lower() != "b" or a.lower() != "c":
        a = input("\n\nAntwoord: ")
        if a == "a" or a == "A":
            t2()
        elif a == "b" or a == "B":
            t3()
        elif a == "c" or a == "C":
            t4()
        else:
            print("Voer A, B of C in.")

def q2():
    print("\n" + "Vraag 2".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "q2" + ".txt") + "\n\n", 0.01, 0.08)

    slowPrint("A. Ja".center(100), 0.01, 0.02)
    slowPrint("B. Nee".center(100), 0.01, 0.02)

    a = ""
    
    while a.lower() != "a" or a.lower() != "b":
        a = input("\n\nAntwoord: ")
        if a == "a" or a == "A":
            t5()
        elif a == "b" or a == "B":
            t6()
        else:
            print("Voer A of B in.")
def q3():
    print("\n" + "Vraag 3".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "q3" + ".txt") + "\n\n", 0.01, 0.08)

    slowPrint("A. Ja".center(100), 0.01, 0.02)
    slowPrint("B. Nee".center(100), 0.01, 0.02)

    a = ""
    
    while a.lower() != "a" or a.lower() != "b":
        a = input("\n\nAntwoord: ")
        if a == "a" or a == "A":
            t7()
        elif a == "b" or a == "B":
            t6() # Flowchart says to lead to t8, but it doesn't exist; it leads to t6
        else:
            print("Voer A of B in.")

# q4 does not exist: t4() leads straight to q10()
def q5():
    print("\n" + "Vraag 5".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "q5" + ".txt") + "\n\n", 0.01, 0.08)

    slowPrint("A. Ja".center(100), 0.01, 0.02)
    slowPrint("B. Nee".center(100), 0.01, 0.02)

    a = ""
    
    while a.lower() != "a" or a.lower() != "b":
        a = input("\n\nAntwoord: ")
        if a == "a" or a == "A":
            t9()
        elif a == "b" or a == "B":
            t6()
        else:
            print("Voer A of B in.")

def q6():
    print("\n" + "Vraag 6".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "q6" + ".txt") + "\n\n", 0.01, 0.08)

    slowPrint("A. Waarheid".center(100), 0.01, 0.02)
    slowPrint("B. Gerust".center(100), 0.01, 0.02)

    a = ""
    
    while a.lower() != "a" or a.lower() != "b":
        a = input("\n\nAntwoord: ")
        if a == "a" or a == "A":
            t11()
        elif a == "b" or a == "B":
            t10()
        else:
            print("Voer A of B in.")

def q7():
    print("\n" + "Vraag 7".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "q7" + ".txt") + "\n\n", 0.01, 0.08)

    slowPrint("A. Supermarkt".center(100), 0.01, 0.02)
    slowPrint("B. Naar huis".center(100), 0.01, 0.02)

    a = ""
    
    while a.lower() != "a" or a.lower() != "b":
        a = input("\n\nAntwoord: ")
        if a == "a" or a == "A":
            t6()
        elif a == "b" or a == "B":
            t9()
        else:
            print("Voer A of B in.")

# There is no q8
def q9():
    print("\n" + "Vraag 9".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "q9" + ".txt") + "\n\n", 0.01, 0.08)

    slowPrint("A. Waarheid".center(100), 0.01, 0.02)
    slowPrint("B. Smoes".center(100), 0.01, 0.02)

    a = ""
    
    while a.lower() != "a" or a.lower() != "b":
        a = input("\n\nAntwoord: ")
        if a == "a" or a == "A":
            t11()
        elif a == "b" or a == "B":
            t10()
        else:
            print("Voer A of B in.")

def q10():
    print("\n" + "Vraag 10".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "q10" + ".txt") + "\n\n", 0.01, 0.08)

    slowPrint("A. Ja".center(100), 0.01, 0.02)
    slowPrint("B. Nee".center(100), 0.01, 0.02)

    a = ""
    
    while a.lower() != "a" or a.lower() != "b":
        a = input("\n\nAntwoord: ")
        if a == "a" or a == "A":
            t12()
        elif a == "b" or a == "B":
            t13()
        else:
            print("Voer A of B in.")

# There is no q11
inventory = [""]
def q12():
    global inventory

    print("\n" + "Vraag 12".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "q12" + ".txt") + "\n\n", 0.01, 0.08)

    slowPrint("A. Fotolijstje met een foto van je gezin".center(100), 0.01, 0.02)
    slowPrint("B. Je mobiele telefoon".center(100), 0.01, 0.02)
    slowPrint("C. De knuffelbeer die je sinds je geboorte hebt".center(100), 0.01, 0.02)

    a = ""
    
    while a.lower() != "a" or a.lower() != "b" or a.lower() != "c":
        a = input("\n\nAntwoord: ")
        if a == "a" or a == "A":
            inventory[0] = "photo"
            print("\nJe hebt gekozen om de foto mee te nemen. [εϊз]")
            t18()
        elif a == "b" or a == "B":
            inventory[0] = "phone"
            print("\nJe hebt gekozen om de telefoon mee te nemen. [εϊз]")
            t18()
        elif a == "c" or a == "C":
            inventory[0] = "bear"
            print("\nJe hebt gekozen om de knuffelbeer mee te nemen. [εϊз]")
            t18()
        else:
            print("Voer A, B of C in.")

def q13():
    print("\n" + "Vraag 13".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "q13" + ".txt") + "\n\n", 0.01, 0.08)

    slowPrint("A. Ja".center(100), 0.01, 0.02)
    slowPrint("B. Nee".center(100), 0.01, 0.02)

    a = ""
    
    while a.lower() != "a" or a.lower() != "b":
        a = input("\n\nAntwoord: ")
        if a == "a" or a == "A":
            t15()
        elif a == "b" or a == "B":
            t14()
        else:
            print("Voer A of B in.")

# There is no q14
def q15():
    print("\n" + "Vraag 15".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "q15" + ".txt") + "\n\n", 0.01, 0.08)

    slowPrint("A. Ja".center(100), 0.01, 0.02)
    slowPrint("B. Nee".center(100), 0.01, 0.02)

    a = ""
    
    while a.lower() != "a" or a.lower() != "b":
        a = input("\n\nAntwoord: ")
        if a == "a" or a == "A":
            t17()
        elif a == "b" or a == "B":
            t16()
        else:
            print("Voer A of B in.")

# There is no q16 + q17; t16 and t17 lead directly to endings
def q18():
    print("\n" + "Vraag 18".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "q18" + ".txt") + "\n\n", 0.01, 0.08)

    slowPrint("A. Ja".center(100), 0.01, 0.02)
    slowPrint("B. Nee".center(100), 0.01, 0.02)

    a = ""
    
    while a.lower() != "a" or a.lower() != "b":
        a = input("\n\nAntwoord: ")
        if a == "a" or a == "A":
            t19()
        elif a == "b" or a == "B":
            t20()
        else:
            print("Voer A of B in.")

# There is no q19 (t19 directly to ending), no q20 (replaced by b1) and no q21 (t21 directly to ending)
def q22():
    print("\n" + "Vraag 22".center(100, "-") + "\n")
    slowPrint(getText("txts/" + "q22" + ".txt") + "\n\n", 0.01, 0.08)

    slowPrint("A. Hoop".center(100), 0.01, 0.02)
    slowPrint("B. Onzeker".center(100), 0.01, 0.02)

    a = ""
    
    while a.lower() != "a" or a.lower() != "b":
        a = input("\n\nAntwoord: ")
        if a == "a" or a == "A":
            t23()
        elif a == "b" or a == "B":
            t24()
        else:
            print("Voer A of B in.")


# Branches
# ----------------------------

def b1():
    if inventory[0] == "phone":
        t22()
    else:
        t21()


# Endings
# ----------------------------

def e1():
    changeScreenSize(34, 40)

    print("\n" + "Einde".center(34, "-") + "\n")
    print(getText("txtimgs/gravestone.txt"))
    slowPrint("\n\n" + getText("txts/" + "e1" + ".txt") + "\n\n", 0.01, 0.08)
    input("\n[Druk op enter om terug naar het begin te gaan]")
    clearScreen()
    t1()

def e2():
    changeScreenSize(34, 40)

    print("\n" + "Einde".center(34, "-") + "\n")
    print(getText("txtimgs/gravestone.txt"))
    slowPrint("\n\n" + getText("txts/" + "e2" + ".txt") + "\n\n", 0.01, 0.08)
    input("\n[Druk op enter om terug naar het begin te gaan]")
    clearScreen()
    t1()

def e3():
    changeScreenSize(34, 40)

    print("\n" + "Einde".center(34, "-") + "\n")
    print(getText("txtimgs/gravestone.txt"))
    slowPrint("\n\n" + getText("txts/" + "e3" + ".txt") + "\n\n", 0.01, 0.08)
    input("\n[Druk op enter om terug naar het begin te gaan]")
    clearScreen()
    t1()

def e4():
    changeScreenSize(34, 40)

    print("\n" + "Einde".center(34, "-") + "\n")
    print(getText("txtimgs/gravestone.txt"))
    slowPrint("\n\n" + getText("txts/" + "e4" + ".txt") + "\n\n", 0.01, 0.08)
    input("\n[Druk op enter om terug naar het begin te gaan]")
    clearScreen()
    t1()

def e5():
    changeScreenSize(34, 40)

    print("\n" + "Einde".center(34, "-") + "\n")
    print(getText("txtimgs/yingyang.txt"))
    slowPrint("\n\n" + getText("txts/" + "e5" + ".txt") + "\n\n", 0.01, 0.08)
    input("\n[Druk op enter om terug naar het begin te gaan]")
    clearScreen()
    t1()

def e6():
    changeScreenSize(34, 40)

    print("\n" + "Einde".center(34, "-") + "\n")
    print(getText("txtimgs/yingyang.txt"))
    slowPrint("\n\n" + getText("txts/" + "e6" + ".txt") + "\n\n", 0.01, 0.08)
    input("\n[Druk op enter om terug naar het begin te gaan]")
    clearScreen()
    t1()