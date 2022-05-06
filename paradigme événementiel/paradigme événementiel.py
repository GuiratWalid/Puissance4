# ******************** Le jeu puissance 4 ********************

#Importation des modules
from tkinter import *


#Déclaration des variables globales:
# Déclaration et initialisation de la matrice Grille
Grille = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
L = []
n = 1
tour = 1
message = "C'est le tour du joueur N°1"
fin = False
colonne = ligne = -1

# Création des pions
def creation_circle(x, y, r, nomCanvas,couleur):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return nomCanvas.create_oval(x0, y0, x1, y1,outline=couleur, fill=couleur)

# Initialisation de la matrice graphique
def initialiser():
    for i in range(6):
        x = []
        for j in range(7):
            x.append(creation_circle(50 + j * 70, 50 + 70 * i, 30, monCanvas, "#FA8072"))
        L.append(x)

#callback du menu annuler
def annuler():
    global n,ligne,colonne,label3,tour
    if tour == 1 and n == 1 :
        erreur("Annulation impossible \n Aucun pion est mis dans la matrice")
    else:
        if ligne < 0 :
            ligne = 0
        Grille[ligne][colonne]=0
        L[ligne][colonne]=creation_circle(50 + colonne * 70, 50 + 70 * ligne, 30, monCanvas, "#FA8072")
        if n == 1 :
            message = "C'est le tour du joueur N°2"
            n = 2
            tour -= 1
        elif n == 2 :
            message = "C'est le tour du joueur N°1"
            n = 1
        label3.pack_forget()
        label3 = Label(frame1, text=message, bg='#eeeeee', font=("Courrier", 18, "bold"), fg="#a50a08")
        label3.pack()

#callback du menu aide
def aide():
    aide = Tk()
    aide.geometry("800x700+400+175")
    aide.title("Jeu Puissance 4")
    aide.minsize(400, 400)
    aide.maxsize(400, 400)
    aide.config(background='#eeeeee')
    # affichage du nom du jeu :
    label = Label(aide, text="Jeu Puissance 4", bg='#eeeeee', font=("Courrier", 20, "bold"), fg="#a50a08")
    label.pack(side="top", pady=20)
    # affichage du principe du jeu :
    fichier=open("principe.txt",'r')
    principe=''
    for ligne in fichier:
        principe+= ligne
    label = Label(aide, text=principe, bg='#eeeeee', font=("Courrier", 10, "bold"), fg="#000000")
    label.pack(pady=30)
    aide.mainloop()

#callback du menu nouveau et le bouton reinitialiser
def reinitialiser():
    global tour,fin,message,label3
    tour = 1
    n = 1
    fin = False
    message="C'est le tour du joueur N°1"
    for i in range(6):
        for j in range(7):
            L[i][j] = creation_circle(50 + j * 70, 50 + 70 * i, 30, monCanvas, "#FA8072")
            Grille[i][j]=0
    label3.pack_forget()
    label3 = Label(frame1, text=message, bg='#eeeeee', font=("Courrier", 18, "bold"), fg="#a50a08")
    label3.pack()

#Verifier si le joueur n gagne en insérant un pion à la position indlig,indcol
def gagner(n ,indlig,indcol):
    # test horizantal
    for i in range(4):
        if Grille[indlig][i] == n and Grille[indlig][i] == Grille[indlig][i+1] == Grille[indlig][i+2] == Grille[indlig][i+3]:
            return True
    # test vertical
    for i in range(3):
        if Grille[i][indcol] == n and Grille[i][indcol] == Grille[i+1][indcol] == Grille[i+2][indcol] == Grille[i+3][indcol]:
            return True
    # test diagonal gauche droite
    # initialisation des indices de la premiére case du diagonal différente de 0
    ld = indlig
    cd = indcol
    while ld > 0 and cd > 0 and Grille[ld][cd]!=0:
        ld -= 1
        cd -= 1
        if Grille[ld][cd]==0:
            ld += 1
            cd += 1
            break
    # initialisation des indices de la derniére case du diagonal différente de 0
    la = indlig
    ca = indcol
    while la < 5 and ca < 6:
        la += 1
        ca += 1
        if Grille[la][ca]==0:
            la -= 1
            ca -= 1
            break
    for i, j in zip(range(ld, la - 3 + 1), range(cd, ca - 3 + 1)):
        if Grille[i][j] == n and Grille[i][j] == Grille[i + 1][j + 1] == Grille[i + 2][j + 2] == Grille[i + 3][j + 3]:
            return True
    # test diagonal droite gauche
    # initialisation des indices de la derniére case du diagonal différente de 0
    ld = indlig
    cd = indcol
    while ld > 0 and cd < 6:
        ld -= 1
        cd += 1
        if Grille[ld][cd]==0:
            ld += 1
            cd -= 1
            break
    # initialisation des indices de la premiére case du diagonal différente de 0
    la = indlig
    ca = indcol
    while la < 5 and ca > 0:
        la += 1
        ca -= 1
        if Grille[la][ca]==0:
            la -= 1
            ca += 1
            break

    for i, j in zip(range(ld, la - 3 + 1), range(cd, ca - 3 + 1,-1)):
        if Grille[i][j] == n and Grille[i][j] == Grille[i + 1][j - 1] == Grille[i + 2][j - 2] == Grille[i + 3][j - 3]:
            return True
    return False

# Déterminé l'indice de ligne le plus bas disponible
def indLig(indcol):
    indlig = 0
    while Grille[indlig][indcol]==0 and indlig < 6:
        indlig+=1
        if indlig == 6: break # pour éviter l'indexation en dehors du tableau
    return indlig-1

# Affichage d'une fenetre d'erreur
def erreur(ch):
    erreur = Tk()
    erreur.geometry("550x170+400+300")
    erreur.title("Jeu Puissance 4")
    erreur.minsize(550, 170)
    erreur.maxsize(550, 170)
    erreur.config(background='#eeeeee')
    label = Label(erreur, text=ch, bg='#eeeeee', font=("Courrier", 16, "bold"), fg="#a50a08")
    label.pack(side=TOP,pady=10)
    bouton = Button(erreur, text="Ok", relief=RAISED, cursor="arrow", command=erreur.destroy)
    bouton.pack(side=BOTTOM,pady=20)

#callback du bouton jouer
def jouer():
    global n,ligne,colonne,message,tour,label3,fin,ligne,colonne
    if fin == False:
        if tour < 22 :
            if len(entry1.get())==0:
                erreur("L'indice ne doit pas être-vide .\n Veuillez choisir un indice entre 1 et 7")
            elif not str(entry1.get()).isdigit():
                erreur("L'indice doit-être un entier .\n Veuillez choisir un indice entre 1 et 7")
            else:
                colonne = int(entry1.get())-1
                if not (colonne in range(7)):
                     erreur("\n L'indice de la colonne est faux .\n Veuillez choisir un indice entre 1 et 7")
                else:
                    ligne = indLig(colonne)
                    if ligne == -1:  # si la case choisie n'est pas vide refaire la saisie des indices
                        erreur("\n La colonne choisie n'est pas libre ,\n Veuillez choisir une autre colonne  ")
                    else:
                        Grille[ligne][colonne] = n  # mettre le numero de joueur dans la case choisie
                        if n == 1:
                            L[ligne][colonne] = creation_circle(50 + colonne * 70, 50 + ligne * 70, 28, monCanvas, "#000000")
                            if gagner(1,ligne,colonne):
                                message="Le joueur N°1 est le vainqueur"
                                fin = True
                            else:
                                n = 2
                                message = "C'est le tour du joueur N°2"
                        else:
                            tour += 1 # incrémentation de numero de tour
                            L[ligne][colonne] = creation_circle(50 + colonne * 70, 50 + ligne * 70, 28, monCanvas, "#FFFFFF")
                            if gagner(2,ligne,colonne):
                                message ="Le joueur N°2 est le vainqueur"
                                fin = True
                            else:
                                n = 1
                                message = "C'est le tour du joueur N°1"
        else:
            message = " Ooops !!\n Le jeu est terminé \n et il n'y a pas de vainqueur "
            fin = True
        label3.pack_forget()
        label3 = Label(frame1, text=message, bg='#eeeeee', font=("Courrier", 18, "bold"), fg="#a50a08")
        label3.pack()

if __name__=='__main__':
    fenetre = Tk()
    fenetre.geometry("1000x700")
    fenetre.title("Jeu Puissance 4")
    fenetre.minsize(1000, 700)
    fenetre.config(background='#eeeeee')
    img = PhotoImage(file='logo.ico') #çà fonctionne sur Ubuntu 20.04
    fenetre.tk.call('wm', 'iconphoto', fenetre._w, img)
    # Definition d'un menu
    menubar = Menu(fenetre)
    # Fichier
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Nouveau", command=reinitialiser)
    menu1.add_separator()
    menu1.add_command(label="Quitter", command=fenetre.destroy)
    menubar.add_cascade(label="Fichier", menu=menu1)
    # Editer
    menu2 = Menu(menubar, tearoff=0)
    menu2.add_command(label="Annuler", command=annuler)
    menubar.add_cascade(label="Editer", menu=menu2)
    # Aide
    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="A propos", command=aide)
    menubar.add_cascade(label="Aide", menu=menu3)
    # Affichage du menu
    fenetre.config(menu=menubar)
    # affichage du nom du jeu :
    label = Label(fenetre, text="Jeu Puissance 4", bg='#eeeeee', font=("Courrier", 20, "bold"), fg="#a50a08")
    label.pack(side="top", pady=20)
    # création des cercles du jeux :
    monCanvas = Canvas(fenetre, width=520, height=450, bg="#B22222")
    monCanvas.pack(side=LEFT, padx=15, pady=5)
    initialiser()
    frame1 = Frame(fenetre, bg='#eeeeee')
    btn1 = Button(frame1, text="Réinitialiser", relief=RAISED, cursor="arrow",command=reinitialiser)
    btn1.pack(pady=50)
    label1 = Label(frame1, text="Colonne : ", bg='#eeeeee', font=("Courrier", 15, "bold"), fg="#582900")
    label1.pack(pady=15)
    entry1 = Entry(frame1, bg='#eeeeee', font=("Courrier", 15, "bold"))
    entry1.pack(pady=20)
    btn2 = Button(frame1, text="Jouer", relief=RAISED, cursor="arrow", command=jouer)
    btn2.pack(pady=50)
    frame1.pack(side=RIGHT, padx=15, pady=10)
    label3 = Label(frame1, text=message, bg='#eeeeee', font=("Courrier", 18, "bold"), fg="#a50a08")
    label3.pack()
    fenetre.mainloop()
