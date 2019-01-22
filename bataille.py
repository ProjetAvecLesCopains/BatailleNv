##############################################
# Auteur : Boillaud Sauvinet Orliange        #
# le 24/09/18                                #
# OS Windows 10, Python 3.7.2 32 bits        #
# Titre : Bataille Navale                    #
# Licence GPL                                #
##############################################
# Importation des fonction externes

from tkinter import *

##############################################
# Définitions locales de fonctions

def traceCercle(): #fonction qui sert a tracer les cercles
    global xcase,ycase
    r=15 #rayon du cercle
    x=x+1
    return can.create_oval(xcase-r, ycase-r, xcase+r, ycase+r, fill='red',outline='black')


def pointeur(event):
    x=int(event.x)
    y=int(event.y)

    if x <= pas*1 :
        numcasex=1
    elif x <= pas*2 :
        numcasex=2
    elif x <= pas*3 :
        numcasex=3
    elif x <= pas*4 :
        numcasex=4
    elif x <= pas*5 :
        numcasex=5
    elif x <= pas*6 :
        numcasex=6
    elif x <= pas*7 :
        numcasex=7
    elif x <= pas*8 :
        numcasex=8
    elif x <= pas*9 :
        numcasex=9
    elif x <= pas*10 :
        numcasex=10

    if y <= pas*1 :
        numcasey=1
    elif y <= pas*2 :
        numcasey=2
    elif y <= pas*3 :
        numcasey=3
    elif y <= pas*4 :
        numcasey=4
    elif y <= pas*5 :
        numcasey=5
    elif y <= pas*6 :
        numcasey=6
    elif y <= pas*7 :
        numcasey=7
    elif y <= pas*8 :
        numcasey=8
    elif y <= pas*9 :
        numcasey=9
    elif y <= pas*10 :
        numcasey=10

    xcase=pas*(numcasex-1)+(1/2)*pas

    ycase=pas*(numcasey-1)+(1/2)*pas

    r=15 #rayon du cercle
    xcase=xcase+1
    return can.create_oval(xcase-r, ycase-r, xcase+r, ycase+r, fill='red',outline='black')

##############################################
# Interface graphique

fen=Tk()
fen.title('Bataille Navale')
cote=400

can=Canvas(fen,bg="white", height=cote, width=cote)
can.grid(row=1,column=1,rowspan=5,columnspan=5)

nbrcase=10
pas=cote/nbrcase

x=0
while (x<=nbrcase):
    can.create_line(0,pas*x,cote,pas*x,fill='black')
    x=x+1
y=0
while (y<=nbrcase):
    can.create_line(pas*y,0,pas*y,cote,fill='black')
    y=y+1

#text en bas de la fenetre
chaineProposition="clique Sur une case "
testProposition=Label(fen,text=chaineProposition)
testProposition.grid(row=6,column=3)

# Config de la souris sur la fenetre
fen.bind("<Button-1>", pointeur)


##############################################
# Corps principal du programme

fen.mainloop() # lance le programme
