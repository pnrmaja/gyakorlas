import random
import math

def veletlen():
    i: int = 0
    while i < 110:
        szam:int =math.floor(random.random()*21+10)
        print(szam, end=" ")
        i+=1

def feladat1():
    i=int= 0
    while i < 5:
        szam:int = math.floor(random.random()*90+1)
        print(szam, end="  ")
        i+=1

def feladat2():
    szam:int= math.floor(random.random()*90+10)
    if (szam%2==0):
        print(f"A szám páros {szam}")
    else:
        print(f"Ez a szám páratlan {szam}")




def feladat3():
    i=int=0
    db=0
    while i < 15:
        szam:int = math.floor(random.random()*2)
        print(f"{szam}", end=" ")
        if(szam>0):
            db = db + 1
        else:
           szam<0

        i+=1
    print(f"ennyi egyest generált: {db}")


def feladat4():

    eredeti: int = math.floor(random.random() *10 + 1)
    szam=eredeti
    print(eredeti, end=" ")
    szam=szam*3
    szam=szam-15
    szam=szam/6
    szam=szam*2
    szam=szam-eredeti

    if(szam==5):
        print(f" {szam} Ez a szám egyenlő 5-el")

    else:
        print(f"{szam} A szám nem egyenlő 5-el")


def feladat5(szoveg):
    hossz=len(szoveg)
    if (hossz>=5):
        print(szoveg[4].upper())

















