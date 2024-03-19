
# import Grille
#ici on va utiliser de la programmation dynamique pour retrouver UN plus cours chemin de manière optimale.

#relation de récurence: le plus cours chemin pour atteindre (i, j) != (1, 1)
    # - si i = 1 : le chemin de (i-1, j) + mur_gauche
    # - si j = 1 : le chemin de (i, j-1) + mur_haut
    # - sinon : on calcule le cout minimal entre cout_haut et cout_gauche,
    #     la réponse est : le chemin correspondant + mur_correspondant




n, m = 3, 4


def minimum(dico):
    m=float('inf')
    for k in dico:
        if dico[k] < m:
            m=dico[k]
            i=k
    return i




















def dijkstra_pred(G,s):
    D={} 
    d={k: float('inf') for k in G} 
    d[s]=0 
    P={}
    while len(d)>0: 
        k=minimum(d) 
        for mur in G[k]: 
            cel_v = G[k][mur][0]
            ep = G[k][mur][1]
            # cel_v, ep = G[k][mur]
            if cel_v not in D:
                if d[cel_v]>d[k]+ep:
                    d[cel_v]=d[k]+ep
                    P[cel_v]=k
        D[k]=d[k]
        del(d[k])
    return D, P


def bellman_ford(G, s):
    d={k: float('inf') for k in G}  
    P={}
    d[s]=0   
    fini=False
    while not fini:
        fini=True
        for cel in G:
            for mur in G[cel]:
                cel_v, ep = G[cel][mur]  
                if d[cel]+ep < d[cel_v]:
                    d[cel_v] = d[cel]+ep
                    P[cel_v]=cel
                    fini=False
    return d, P















def plus_court_chemin(G, n, m, algo='jidks'):
    if algo == 'bel':
        d, P = bellman_ford(G, (1, 1))
    else:
        d, P = dijkstra_pred(G, (1, 1))
    
    cout = d[(n, m)]
    cel = (n, m)
    c = [cel]
    while cel != (1, 1):
        c.append(P[cel])
        cel = P[cel]
    c.reverse()
    return c, cout

grille = {
    (1, 1): {'g': [(1, 1), 4], 'h': [(1, 1), 4], 'd': [(1, 2), 5], 'b': [(2, 1), 2]},
    (1, 2): {'g': [(1, 1), 2], 'h': [(1, 2), 1], 'd': [(1, 3), 5], 'b': [(2, 2), 2]}, 
    (1, 3): {'g': [(1, 2), 1], 'h': [(1, 3), 4], 'd': [(1, 4), 2], 'b': [(2, 3), 5]}, 
    (1, 4): {'g': [(1, 3), 5], 'h': [(1, 4), 3], 'd': [(1, 4), 1], 'b': [(2, 4), 5]}, 
    (2, 1): {'g': [(2, 1), 1], 'h': [(1, 1), 1], 'd': [(2, 2), 3], 'b': [(3, 1), 3]}, 
    (2, 2): {'g': [(2, 1), 4], 'h': [(1, 2), 2], 'd': [(2, 3), 1], 'b': [(3, 2), 3]}, 
    (2, 3): {'g': [(2, 2), 2], 'h': [(1, 3), 1], 'd': [(2, 4), 4], 'b': [(3, 3), 4]}, 
    (2, 4): {'g': [(2, 3), 5], 'h': [(1, 4), 3], 'd': [(2, 4), 5], 'b': [(3, 4), 1]}, 
    (3, 1): {'g': [(3, 1), 5], 'h': [(2, 1), 4], 'd': [(3, 2), 3], 'b': [(3, 1), 5]}, 
    (3, 2): {'g': [(3, 1), 2], 'h': [(2, 2), 2], 'd': [(3, 3), 1], 'b': [(3, 2), 3]}, 
    (3, 3): {'g': [(3, 2), 3], 'h': [(2, 3), 4], 'd': [(3, 4), 1], 'b': [(3, 3), 2]}, 
    (3, 4): {'g': [(3, 3), 2], 'h': [(2, 4), 5], 'd': [(3, 4), 3], 'b': [(3, 4), 5]}
}
# print(bellman_ford(grille, (1, 1)))