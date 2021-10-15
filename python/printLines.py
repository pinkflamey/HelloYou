from time import sleep

def printLines(name, span):
    f=open(name)
    for line in f:
        print(line.center(span))
    f.close()