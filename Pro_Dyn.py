#on utilisera dans ce modo de la programation dynamique

import Grille as G

# grille = { 
#     (1, 1): {
#         'g': [(1, 1), 1],
#         'h' : [(1, 1), 1],
#         'd' : [(1, 2), 5],
#         'b' : [(1, 5), 2]
#     },
#     (1, 2): {
#         'g': [(1, 1), 5],
#         'h' : [(1, 2), 2],
#         'd' : [(1, 3), 1],
#         'b' : [(1, 5), 3]
#     },
#     # { ... }
# }

# Gr = G.creer_grille(3, 4)

def dynamique_const(grille, n, m):
    Tab_PCC = [] #il aura la forme [chemin, cout] où chemin est un tab de couples

    #parcourt de chaque élement de la grille, de droite à gauche, du haut vers le bas
    for l in range(1, n+1):
        for c in range(1, m+1):
            if l == 1 and c == 1:
                Tab_PCC.append( [ [(1, 1)], 0 ] )
            elif l == 1 :
                chemin = #je ne sais plus !
                Tab_PCC.append( [ chemin, cout + grille[(l,c)]['g'][2] ] )