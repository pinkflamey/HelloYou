from os import system
from sys import platform

def changeScreenSize(col, lin):
    if platform == "win32":
        system("mode con: cols="+str(col)+" lines="+str(lin))
    else:
        system("resize -s "+str(lin)+" "+str(col))