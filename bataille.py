from tkinter import *
Menu=Tk()
Fond=PhotoImage(file="Fond page d'accueil.gif")
boutonjouer=Button(Menu,image=Fond,command=Menu.destroy)
boutonjouer.grid(row=3,column=3,rowspan=3,columnspan=3)
Menu.mainloop()

def apprendrecoor(listx1,listy2,listy1,listx2,ListJoueur1X,ListJoueur1Y,ListJoueur2X,ListJoueur2Y,x,y):
    global Compteur,joueur,Couleur,PassageJoueur2,PassageAujeu,bat2,bat3,VA,abc

    if (Compteur<2.5) and (PassageAujeu==0):
        Compteur=Compteur+1
        Label2.config(text='il reste encore {} case a mettre'.format(3-Compteur))
        if PassageJoueur2==0:
            listx1.append(x)
            listy1.append(y)
            GrilleJoueur1[x][y]=1
        else:
            listx2.append(x)
            listy2.append(y)
            GrilleJoueur2[x][y]=1
        Case[x][y].config(background=Couleur,state='disable')

    if (Compteur>=3) and (PassageAujeu==0):
        Label2.config(text='')
        if len(ListJoueur1X)>=6:
            if PassageJoueur2==0:
                bat2=0
                bat3=0
                print('la liste du joueur 1 est pleine')
                print('len ListJoueur1X {} \n'.format(len(ListJoueur1X[0])))
                for i in range(len(Case)):
                    for j in range(len(Case[i])):
                        x=Case[i][j]
                        x.config(background='white',state='normal')
                Label.config(text="C'est au tour du joueur 2 de jouer")
                PassageJoueur2=1
                boutonbateau5.config(state='normal')
                boutonbateau4.config(state='normal')
                boutonbateau3.config(state='normal')
                boutonbateau2.config(state='normal')
                ListJoueur1.append(ListJoueur1X[0])
                Couleur='red'
            else:
                if (len(ListJoueur2X)>=6) and (PassageAujeu==0):
                    for i in range(len(Case)):
                        for j in range(len(Case[i])):
                            x=Case[i][j]
                            x.config(background='white',state='normal')
                    PassageAujeu=1
                    Label.config(text="Le joueur 2 a egalement finit")
                    ListJoueur2.append(ListJoueur2X[0])
                    ListJoueur2.append(ListJoueur2Y[0])
                    print(ListJoueur1,ListJoueur2)
                else:
                    ListJoueur2Y.extend([listy2])
                    ListJoueur2X.extend([listx2])
                    Label.config(text="Le joueur 2 joue")
                    print("nombre d'element de la liste {} \n".format(len(ListJoueur2X)))
        else:
            ListJoueur1X.extend([listx1])
            ListJoueur1Y.extend([listy1])
            print("nombre d'element de la liste {} \n".format(len(ListJoueur1X)))
            Label.config(text="Le joueur 1 joue")

    if PassageAujeu==1:
        abc=VA%2
        FonctionAtt(abc,x,y)
        BoutonJouer.grid(row=15,column=3,columnspan=2)

def ajoutvaleur():
    global VA
    VA=VA+1
    
def FonctionAtt(abc,x,y):
    global Couleur

    if abc==0:       #joueur1
        Label.config(text="Le joueur 1 joue")
        Couleur="red"
        if (GrilleJoueur2[int(x)][int(y)])==1:
            Label2.config(text='Vaisseau toucher')
        else:
            Label2.config(text=' Aucun Vaisseau toucher ')

    else:           #joueur 2
        Label.config(text="Le joueur 2 joue")
        Couleur="green"
        if (GrilleJoueur1[int(x)][int(y)])==1:
            Label2.config(text='Vaisseau toucher')
        else:
            Label2.config(text=' Aucun Vaisseau toucher ')

def bateau3():
    global Compteur,bat3
    for bat in range (0,1):
        Compteur=0
        if bat3==1:
            boutonbateau3.config(state='disable')
        else:
            bat3=bat3+1

def bateau2():
    global Compteur,bat2
    for bat in range (0,1):
        Compteur=1
        if bat2==1:
            boutonbateau2.config(state='disable')
        else:
            bat2=bat2+1

def bateau4():
    global Compteur
    Compteur=-1
    boutonbateau4.config(state='disable')

def bateau5():
    global Compteur
    Compteur=-2
    boutonbateau5.config(state='disable')

fen=Tk()

Compteur=10
n,p=10,10
listx1=[]
listy1=[]
listy2=[]
listx2=[]
Case=[]
bat2=0
bat3=0
Couleur='green'
PassageJoueur2=0
joueur=1
PassageAujeu=0
ListJoueur1X=[]
ListJoueur2X=[]
ListJoueur1Y=[]
ListJoueur2Y=[]
ListJoueur1=[]
ListJoueur2=[]
VA=0
abc=0
GrilleJoueur1=[]
GrilleJoueur2=[]
FondCase=PhotoImage(file="espace.gif")

for i in range(0,n):
    Case.append([])
    GrilleJoueur1.append([])
    GrilleJoueur2.append([])
    for j in range(0,p):
        Case[i].append(Button (fen, image=FondCase,command=lambda x=i,
        y=j,testx=0 ,testy=0: apprendrecoor(listx1,listy2,listy1,listx2,ListJoueur1X,ListJoueur1Y,ListJoueur2X,ListJoueur2Y,x,y)
        ,width=50,height=50,activebackground="silver",background="white"))
        Case[i][j].grid(row=i,column=j)
        GrilleJoueur1[i].append(0)
        GrilleJoueur2[i].append(0)

BoutonJouer=Button(fen,text=" Joueur Suivant ",command=ajoutvaleur)
boutonbateau3=Button(fen,text="Bateau 3 case",command=bateau3)
boutonbateau3.grid(row=12,column=1,columnspan=2)
boutonbateau2=Button(fen,text="Bateau 2 case",command=bateau2)
boutonbateau2.grid(row=12,column=3,columnspan=2)
boutonbateau5=Button(fen,text="Bateau 5 case",command=bateau5)
boutonbateau5.grid(row=13,column=1,columnspan=2)
boutonbateau4=Button(fen,text="Bateau 4 case",command=bateau4)
boutonbateau4.grid(row=13,column=3,columnspan=2)
Label2=Label(fen,text=" ")
Label2.grid(row=14,column=6,columnspan=4)
Label=Label(fen,text="C'est au tour du joueur 1 de jouer ")
Label.grid(row=13,column=6,columnspan=4)

fen.mainloop()
