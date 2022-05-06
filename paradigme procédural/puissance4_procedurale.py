# ******************** Le jeu puissance 4 ********************



# Déclaration et initialisation de la matrice Grille
Grille = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

# Affichage personnalisé de la matrice Grille
def affiche():
    print("     0   1   2   3   4   5   6  ") # Affichage des indices des colonnes
    print("   "+"-"*29) # Affichage du premier trait horizantal
    for i in range(6):
        print(i,end="  | ") # Affichage des indices des lignes et le premier trait vertical
        for j in range(7):
            print(Grille[i][j],end=" | ") # Affichage de l'élément de l'iéme ligne et jéme colonne ainsi que les traits horizantaux
        print() # Un retour à la ligne
        print("   "+"-" * 29) # Affichage des traits horizantaux


# Déterminé l'indice de ligne le plus bas disponible
def indLig(indcol):
    indlig = 0
    while Grille[indlig][indcol]==0 and indlig < 6:
        indlig+=1
        if indlig == 6: break # pour éviter l'indexation en dehors du tableau
    return indlig-1


# La saisie d'un indice colonne avec un test s'il est entre 0 et 6
def saisirIndCol():
    ch = input(" Choisissez une colonne : ")
    if len(ch) == 0:
        raise ValueError("L'indice de colonne ne doit pas être vide")
    elif not ch.isdigit():
        raise ValueError("L'indice de colonne doit être un entier")
    while not int(ch) in range(7):
        if len(ch)==0:
            raise ValueError("L'indice de colonne ne doit pas être vide")
        elif not ch.isdigit():
            raise ValueError("L'indice de colonne doit être un entier")
        print("L'indice de la colonne est faux . Veuillez choisir un indice entre 0 et 6")
        ch=input(" Choisissez une colonne : ")
    return int(ch)


# Le joueur numero n va jouer son tour
def jouer(n):
    indcol = saisirIndCol()
    indlig = indLig(indcol)
    while indlig == -1 : # si la colonne choisie n'est pas vide refaire la saisie d'une autre colonne
        print(" La colonne que vous avez choisi n'est pas libre , veuillez choisir une autre case : ")
        indcol = saisirIndCol()
        indlig = indLig(indcol)
    Grille[indlig][indcol] = n # mettre le numero de joueur dans la case choisie
    return indlig,indcol

# Tester si le joueur n a gagné en mettant un pion à la position(indlig,indcol)
def gagner(n,indlig,indcol):
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

# Saisir les noms des joueurs
def joueurs():
    j1 = input("Saisir le nom du joueur n°1 : ")
    while len(j1)==0:
        j1 = input("il faut saisir le nom du joueur n°1 : ")
    j2 = input("Saisir le nom du joueur n°2 : ")
    while len(j2)==0:
        j2 = input("il faut saisir le nom du joueur n°1 : ")
    return j1,j2

if __name__ == '__main__':
    tour = 1 # Compteur pour compter les nombres de tours
    joueur1,joueur2 = joueurs()
    while tour <= 21 :
        affiche() # affichage de la matrice Grille
        print("C'est le tour de {}: ".format(joueur1))
        indlig,indcol=jouer(1) # le premier joueur commence à jouer son tour
        if gagner(1,indlig,indcol):
            affiche()  # affichage de la matrice Grille
            print(joueur1+" est le vainqueur ")
            break
        affiche() # affichage de la matrice Grille
        print("C'est le tour de {}: ".format(joueur1))
        indlig,indcol=jouer(2) # le deuxiéme joueur commence à jouer son tour
        if gagner(2,indlig,indcol):
            affiche()  # affichage de la matrice Grille
            print(joueur2+" est le vainqueur ")
            break
        tour += 1 # incrémentation de numero de tour
    if tour > 21:
        print(" Ooops !! Le jeu est terminé et il n'y a pas de vainqueur ")
