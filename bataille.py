##############################################
# Auteur : Boillaud Sauvinet Orliange        #
# le 24/09/18                                #
# OS Windows 10, Python 3.6 32 bits          #
# Titre : Bataille Navale                    #
# Licence GPL                                #
##############################################
# Importation des fonction externes

from tkinter import *

##############################################
# Définitions locales de fonctions

def traceCercle(): #fonction qui sert a tracer les cercles 
    global x,y
    r=15 #rayon du cercle
    x=x+1 
    return can.create_oval(x-r, y-r, x+r, y+r, fill='red',outline='black')

def CoordX(evt): #ce qui transforme  des coordonner en X en coordonner sur le canvas
    global x
    x=int(saisieProposition.get())
    x=pas*(x-1)+(1/2)*pas

def CoordY(evt): #ce qui transforme  des coordonner en Y en coordonner sur le canvas
    global y
    y=int(saisieProposition2.get())
    y=pas*(y-1)+(1/2)*pas

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

#text au dessus de boite de saisie
chaineProposition="Saisie ta proposition et appuie sur entrée"
testProposition=Label(fen,text=chaineProposition)
testProposition.grid(row=6,column=3)

# Text a cote de la boite de saisie X
chaineX="X"
textX=Label(fen,text=chaineX)
textX.grid(row=7,column=2,sticky='e')
#Boite de saisie
saisieProposition=Entry(fen)
saisieProposition.config(justify='left')
saisieProposition.grid(row=7,column=3)
saisieProposition.bind('<Return>',CoordX)
# Text a cote de la boite de saisie Y
chaineY="Y"
textY=Label(fen,text=chaineY)
textY.grid(row=8,column=2,sticky='e')
#Boite de saisie
saisieProposition2=Entry(fen)
saisieProposition2.config(justify='left')
saisieProposition2.grid(row=8,column=3)
saisieProposition2.bind('<Return>',CoordY)
#Bouton tracer en bas a droite
boutonCercle=Button(fen,text='Tracer',command=traceCercle,capstyle=round)
boutonCercle.grid(column=5,row=9)

##############################################
# Corps principal du programme

fen.mainloop() # lance le programme
