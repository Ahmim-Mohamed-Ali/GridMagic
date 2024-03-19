import random



# modèle informatique de la grille

# matrcie d'adjacence:
# M = []


# grille = [
#     { 
#         'num': 1, 
#         'position': [0, 0], 
#         'voisins':[ 
#             {'num':1, 'mur':1}, 
#             {'num':1, 'mur':M[1, 1]}, 
#             {'num': 2, 'mur': M[1, 2]}, 
#             {'num': 5, 'mur': 2}
#         ]
#     }, 
#     {
#         # ...
#     }
# ]


# #autre maniere
# grille = [
#     { 
#         'num': 1, 
#         'position': [0, 0], 
#         'voisins':[ [1, 1], [1, 1], [2, 5], [5, 2] ]
#     }, 
#     {
#         # ...
#     }
# ]





# def rand_murs(n, m):
#     murs_générés = [ 'ep1', 'ep2', ..., 'epn' ]
#     return murs_générés




# numéro magique de nb de murs : m = nb de colonnes, n=nb de lignes
# m*3 + m*2*(n-1) + n



# def gen_grille(n, m, tab_ep_murs):
#     ...
#     return grille










#fonction qui génère un nombre aléatoire entre 1 et 5:
def rnd():
    return random.randint(1, 5)














#initialisations
n = 3
m = 4

nb_murs = m*3 + m*2*(n-1) + n
# print(nb_murs)















def gen_tab_ep_alea(n, m):
    #forme du tableau : [ [ep, [cel1, cel2] ], ... ]
    Tab_Murs = []
    #génération des murs de la premières ligne du haut :
    Tab_lignes_haut = []
    for i in range(1, m+1):
        r = rnd()
        Tab_Murs.append([r, [(1, i), (1, i)]])
        # print(r, [(1, i), (1, i)])
    # print("\n")

    #génération des murs de la dérnière ligne du bas :
    Tab_lignes_bas = []
    for i in range(1, m+1):
        r = rnd()
        Tab_Murs.append([r, [(n, i), (n, i)]])
        # print(r, [(n, i), (n, i)])
    # print("\n")

    #génération des murs de la premières colonne du gauche :
    Tab_colonnes_gauche = []
    for i in range(1, n+1):
        r = rnd()
        Tab_Murs.append([r, [(i, 1), (i, 1)]])
        # print(r, [(i, 1), (i, 1)])
    # print("\n")

    #génération des murs de la dérnière colonne du droite :
    Tab_colonnes_droite = []
    for i in range(1, n+1):
        r = rnd()
        Tab_Murs.append([r, [(i, m), (i, m)]])
        # print(r, [(i, m), (i, m)])
    # print("\n")

    #lignes (de la grille) jusqu'à l'avant dérnière:
    Tab_milieu = []
    for l in range(1, n):
        for c in range(1, m):
            r = rnd()
            Tab_Murs.append([r, [(l, c), (l+1, c)]])
            # print(r, [(l, c), (l+1, c)])
            r = rnd()
            Tab_Murs.append([r, [(l, c), (l, c+1)]])
            # print(r, [(l, c), (l, c+1)])
            # print("\n")
        # print("\n")
    # print("\n")


    #dérnière ligne (de la grille):
    Tab_dérnière_ligne = []
    for c in range(1, m):
        r = rnd()
        Tab_Murs.append([r, [(n, c), (n, c+1)]])
        # print(r, [(n, c), (n, c+1)])
    # print("\n")

    #dérnière colonne (de la grille):
    Tab_dérnière_colonne = []
    for l in range(1, n):
        r = rnd()
        Tab_Murs.append([r, [(l, m), (l+1, m)]])
        # print(r, [(l, m), (l, m+1)])
    # print("\n")
    


    # Tab_Murs.append(Tab_lignes_haut)
    # Tab_Murs.append(Tab_lignes_bas)
    # Tab_Murs.append(Tab_colonnes_gauche)
    # Tab_Murs.append(Tab_colonnes_droite)
    # Tab_Murs.append(Tab_milieu)
    # Tab_Murs.append(Tab_dérnière_ligne)
    # Tab_Murs.append(Tab_dérnière_colonne)

    return Tab_Murs







# print(gen_tab_ep_alea(n, m))



def yeux(mur, i):
    ''' fonction qui, à partir d'un mur, retrourne la position de la 1ère cellule par rapport à la 2ème, et vice versa '''
    # if (mur[1][1] == mur[2][1] and mur[1][2] == mur[2][2] + 1):
    #     return "droite"

    # elif (mur[1][1] == mur[2][1] + 1 and mur[1][2] == mur[2][2]):
    #     return "bas"

    if i == 1:
        if (mur[1][0][0] == mur[1][1][0] and mur[1][0][1] == mur[1][1][1] - 1):
            return 'gauche'
        elif (mur[1][0][0] == mur[1][1][0] and mur[1][0][1] == mur[1][1][1] + 1):
            return 'droite'
        elif (mur[1][0][0] == mur[1][1][1] - 1 and mur[1][0][1] == mur[1][1][1]):
            return 'haut'
        elif (mur[1][0][0] == mur[1][1][1] + 1 and mur[1][0][1] == mur[1][1][1]):
            return 'bas'

    if i == 2:
        if (mur[1][0][0] == mur[1][1][0] and mur[1][0][1] == mur[1][1][1] - 1):
            return 'droite'
        elif (mur[1][0][0] == mur[1][1][0] and mur[1][0][1] == mur[1][1][1] + 1):
            return 'gauche'
        elif (mur[1][0][0] == mur[1][1][1] - 1 and mur[1][0][1] == mur[1][1][1]):
            return 'bas'
        elif (mur[1][0][0] == mur[1][1][1] + 1 and mur[1][0][1] == mur[1][1][1]):
            return 'haut'



def trouve_murs(pos, n, m):
    x, y = pos
    Tab_Murs = gen_tab_ep_alea(n, m)
    list_voisins = {'gauche': 0, 'haut': 0, 'droite': 0, 'bas': 0}
    for mur in Tab_Murs:
        # print(mur)
        if (x, y) == mur[1][0]:
            list_voisins[yeux(mur, 1)] = [ mur[1][1], mur[0] ]
            print(yeux(mur, 1))

        elif (x, y) == mur[1][1]:
            list_voisins[yeux(mur, 2)] = [ mur[1][0], mur[0] ]
            print(yeux(mur, 1))

    return list_voisins
        

def grille(n, m):
    # L = gen_tab_ep_alea(n, m)
    grille = []
    for l in range(1, n + 1):
        for c in range(1, m + 1):
            #calculer l'élement à rajouter à la grille
            pos = (l, c)
            voisins = trouve_murs(pos, n, m)
            cel = {
                'pos':pos,
                'voisins': voisins
            }
            grille.append(cel)

    return grille


grille(3, 4)