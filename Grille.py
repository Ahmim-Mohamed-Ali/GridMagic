#ceci sera par la suite une classe portant le nom 'Grille"
#tu trouvera une autre manière (que je juge plus simple) de coder la class grille
#on utilisera un graph non orieté pondéré comme structure de donnée pour coder la dite "grille"
#les sommets du graphe seront les cellules de la grille, ils seront identifiés par leur position
#les aretes du graphe représentent les murs séparant les deux céllules, ces dérières corresponderant
#aux sommets adjacents de l'arete. Enfin le poids de chaque arete repésentera l'épaisseur du mur 
#correspondant

#on va respecter la structure d'une liste d'adjacence, la grille aura donc pour structure:
#un dictionnaire dont les atribus sont les sommets, et les valeurs sont les (aretes + poids), i.e:


grille = { 
    (1, 1): {
        'g': [(1, 1), 1],
        'h' : [(1, 1), 1],
        'd' : [(1, 2), 5],
        'b' : [(1, 5), 2]
    },
    (1, 2): {
        'g': [(1, 1), 5],
        'h' : [(1, 2), 2],
        'd' : [(1, 3), 1],
        'b' : [(1, 5), 3]
    },
    # { ... }
}



# grille = { 
#     (1, 1) : [1, 1, 5, 2],
#     (1, 2) : [5, 2, 1, 3],
#     #...
# }





from random import randint as rnd






def generer_ep():
    '''fonction qui une épaisseur généré aléatoirement, entre 1 et 5'''
    return rnd(1, 5)








#n: nombre de lignes
#m: nombre de colonnes
def creer_grille(n, m):
    '''fonction qui crée la grille et la retourne'''

    #initailisation du dictionnaire grille:
    grille = {}


    

    #ici, pos est un couple (ligne, colonne), ça commence à 1
    def ajouter_cel_à_grille(pos):
        '''fonction qui prépare la cellule courante sour forme d'un dicionnaire, et le rajoute à la grille'''
        
        cel = {}

        if pos[1] == 1:
            cel['g'] = [ pos, generer_ep() ]
        else:
            pos_g = (pos[0], pos[1] - 1)
            cel['g'] = [ pos_g, grille[pos_g]['d'][1] ] #ici grille[pos_g]['d'][1] correspond à l'ep du mur d de la cel gauche

        if pos[0] == 1:
            cel['h'] = [ pos, generer_ep() ]
        else:
            pos_h = (pos[0] - 1, pos[1])
            cel['h'] = [ pos_h, grille[pos_h]['b'][1] ]

        if pos[1] == m:
            cel['d'] = [ pos, generer_ep() ]
        else:
            cel['d'] = [ (pos[0], pos[1] + 1), generer_ep() ]

        if pos[0] == n:
            cel['b'] = [ pos, generer_ep() ]
        else:
            cel['b'] = [ (pos[0] + 1, pos[1]), generer_ep() ]


        grille[pos] = cel
        return cel


    



    #parcourir les lignes, puis les colonnes de la grille:
    for l in range(1, n+1):
        for c in range(1, m+1):
            ajouter_cel_à_grille( (l, c) )
    return grille







#_________________parties tests_______________

# print(generer_ep())

# print(creer_grille(3, 4))

# exemple de sortie de l'appel grille(3, 4):
# grille = {
#     (1, 1): {'g': [(1, 1), 4], 'h': [(1, 1), 4, True], 'd': [(1, 2), 5], 'b': [(2, 1), 2]},
#     (1, 2): {'g': [(1, 1), 2], 'h': [(1, 2), 1], 'd': [(1, 3), 5], 'b': [(2, 2), 2]}, 
#     (1, 3): {'g': [(1, 2), 1], 'h': [(1, 3), 4], 'd': [(1, 4), 2], 'b': [(2, 3), 5]}, 
#     (1, 4): {'g': [(1, 3), 5], 'h': [(1, 4), 3], 'd': [(1, 4), 1], 'b': [(2, 4), 5]}, 
#     (2, 1): {'g': [(2, 1), 1], 'h': [(1, 1), 1], 'd': [(2, 2), 3], 'b': [(3, 1), 3]}, 
#     (2, 2): {'g': [(2, 1), 4], 'h': [(1, 2), 2, True], 'd': [(2, 3), 1], 'b': [(3, 2), 3]}, 
#     (2, 3): {'g': [(2, 2), 2], 'h': [(1, 3), 1], 'd': [(2, 4), 4], 'b': [(3, 3), 4]}, 
#     (2, 4): {'g': [(2, 3), 5], 'h': [(1, 4), 3], 'd': [(2, 4), 5], 'b': [(3, 4), 1]}, 
#     (3, 1): {'g': [(3, 1), 5], 'h': [(2, 1), 4], 'd': [(3, 2), 3], 'b': [(3, 1), 5]}, 
#     (3, 2): {'g': [(3, 1), 2], 'h': [(2, 2), 2, True], 'd': [(3, 3), 1], 'b': [(3, 2), 3]}, 
#     (3, 3): {'g': [(3, 2), 3], 'h': [(2, 3), 4], 'd': [(3, 4), 1], 'b': [(3, 3), 2]}, 
#     (3, 4): {'g': [(3, 3), 2], 'h': [(2, 4), 5], 'd': [(3, 4), 3], 'b': [(3, 4), 5]}
# }
#_______________fin tests__________________