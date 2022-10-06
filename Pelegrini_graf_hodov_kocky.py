import tkinter #knižnica
from random import * #vložil so možnosť používať náhodu 
canvas = tkinter.Canvas(width=600, height=500, bg='white') #údaje pre plátno
canvas.pack() #plátno

pocty = [0]*16 #údaje pre pocty

def kresli():#funkcia na kreslenie
    canvas.delete('stlpce') #mazanie stĺpcov
    for i in range(16): #funkcia pre opakovanie šestnásť krát
        canvas.create_rectangle(50+i*30, 450, 50+i*30+20, 450-pocty[i], #kresleni stĺpcov
                                fill='#4cb050')

def simulacia(): #funkcia na náhodné hody kockou
    global pocet_hodov, pocty #premenné zadefinované pre celí program a nie len pre funkciu
    pocet_hodov -= 1 #odčítame jeden hod
    sucet = 0 #súčet je rovný nule
    for i in range(3): #funkcia pre opakovanie šestnásť krát
        hod = randint(1, 6) #náhodný hod od jedna po šesť
        sucet += hod #do súčtu sa pripočíta výsledná hodnota s náhodného hodu
        pocty[sucet-3] += 1 #do počtu (súčet mínus tri) sa priráta plus jeden
        kresli() #avolá sa funkcia kresli
    if pocet_hodov > 0: #ak je počet hodov väčší ako nula, tak:
        canvas.after(10, simulacia) #po desiatich milisekundách sa zavolá funkcia simulácia

def start(): #funkcia pre štart (zapnutie)
    global pocet_hodov #zadefinuje sa premenná pre celí program
    pocet_hodov = int(entry1.get()) #do premennej pocet_hodov sa vložia údaje vpísané užívaťelom
    simulacia() #zavolá sa funkcia simulácia

#všetky dalšie príkazy sú vykreslované na spodný stred plátna
label1 = tkinter.Label(text='Počet hodov:') #spravíme si nadpis nad Entry
label1.pack() #na plátne sa nám vykreslí nadpis
entry1 = tkinter.Entry() #spravíme si pole pre zadávanie hodnôt
entry1.pack() #na plátne sa nám vykreslí pole pre zadávanie hodnôt
button1 = tkinter.Button(text='štart', command=start) #nastavíme si tlačítko a vpíšeme doňho text
button1.pack() #na plátne sa vykreslí tlačítko
pocet_hodov = 0 #počet hodov sa nám nastaví na nula (vynuluje sa)
