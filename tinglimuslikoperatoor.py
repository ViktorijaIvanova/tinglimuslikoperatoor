from math import *
from random import *
while True:
       try:
           vanus=int(input("pikkus: "))
           if p>0: break
           break
       except:
             print("On vaja arvude tüüp kasutada, mis on suurem kui 0")
while True:
     try:
        l=float(input("Laius: "))
        if l>0: break
     except:
           print("On vaja arvude tüüp kasutada, mis on suurem kui 0")
while True:
    v=input("kas tahad remonti teha? ")
    if v.upper()=="JAH" or v.upper()=="EI" : break
if v.upper()=="JAH":
    hind=input("kui palju maksam m^2")
    hind=l*p*hind
    print(f"remonti hind on {hind}")
else:
    pass


#2 osa
while True:
     nimi1=input("1. mis sinu nimi on? ")
     if nimi1.isalpha(): break
while True:
    nimi2=input("2. mis sinu nimi on? ")
    if nimi2.isalpha(): break
if nimi1=="VIKA" and nimi2=="KARINA": 
    print("neid on täna pinginaabrid")



#1 osa
while True:
    nimi=input("Mis sinu nimi on?")
    if nimi.isalpha(): break
if nimi.upper()=="JUKU":
    while True:
        try:
            vanus=int(input("Kui vana sa oled?"))
            break
        except:
             print("On vaja arvude tüüp kasutada")





    if 0<vanus<6:
        print("tasuta")
    elif 6<=vanus<=14:
        print("lastepilet")
    elif 15<=vanus<65:
        print("täispilet")
    elif 65<=vanus<100:
        print("soduspilet")
    else:
        print("vanus ei soobi!")
else:
    print("Ma otsin Juku!")