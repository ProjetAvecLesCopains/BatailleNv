##############################################
# Auteur : Damien Boillaud le 24/09/18       #
# OS Windows 10, Python 3.6 32 bits          #
# Titre : nombre occurence                   #
# Licence GPL                                #
##############################################
# Importation des fonction externes

from tkinter import *

##############################################
# Définitions locales de fonctions

def traceCercle(x, y):
    r=15
    x=pas*(x-1)
    y=pas*(y-1)
    return can.create_oval(x-r, y-r, x+r, y+r, fill='red',outline='black')

##############################################
# Interface graphique

fen=Tk()
cote=400

can=Canvas(fen,bg="white", height=cote, width=cote)
can.pack()

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
##############################################
# Corps principal du programme

monPion= traceCercle(1,2)
