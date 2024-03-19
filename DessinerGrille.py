import Grille




#exemple
# grille = {
#     (1, 1): {'g': [(1, 1), 4], 'h': [(1, 1), 4], 'd': [(1, 2), 5], 'b': [(2, 1), 2]},
#     (1, 2): {'g': [(1, 1), 2], 'h': [(1, 2), 1], 'd': [(1, 3), 5], 'b': [(2, 2), 2]}, 
#     (1, 3): {'g': [(1, 2), 1], 'h': [(1, 3), 4], 'd': [(1, 4), 2], 'b': [(2, 3), 5]}, 
#     (1, 4): {'g': [(1, 3), 5], 'h': [(1, 4), 3], 'd': [(1, 4), 1], 'b': [(2, 4), 5]}, 
#     (2, 1): {'g': [(2, 1), 1], 'h': [(1, 1), 1], 'd': [(2, 2), 3], 'b': [(3, 1), 3]}, 
#     (2, 2): {'g': [(2, 1), 4], 'h': [(1, 2), 2], 'd': [(2, 3), 1], 'b': [(3, 2), 3]}, 
#     (2, 3): {'g': [(2, 2), 2], 'h': [(1, 3), 1], 'd': [(2, 4), 4], 'b': [(3, 3), 4]}, 
#     (2, 4): {'g': [(2, 3), 5], 'h': [(1, 4), 3], 'd': [(2, 4), 5], 'b': [(3, 4), 1]}, 
#     (3, 1): {'g': [(3, 1), 5], 'h': [(2, 1), 4], 'd': [(3, 2), 3], 'b': [(3, 1), 5]}, 
#     (3, 2): {'g': [(3, 1), 2], 'h': [(2, 2), 2], 'd': [(3, 3), 1], 'b': [(3, 2), 3]}, 
#     (3, 3): {'g': [(3, 2), 3], 'h': [(2, 3), 4], 'd': [(3, 4), 1], 'b': [(3, 3), 2]}, 
#     (3, 4): {'g': [(3, 3), 2], 'h': [(2, 4), 5], 'd': [(3, 4), 3], 'b': [(3, 4), 5]}
# }






#pos commence de (1, 1) et correspand à la position de la tortue à l'instant t
def ep_mur(grille, pos, dir, n, m):
    '''fonction qui prend en paramètre une grille, la position de la tortue et la direction : horizontale ou verticale, 
    et retourne l'épaisseur du mur à dessiner'''
    if dir == 'h':
        if pos[0] == n+1:
            return grille[(n, pos[1])]['b'][1]
        else:
            return grille[pos]['h'][1]
    elif dir == 'v':
        if pos[1] == m+1:
            return grille[(pos[0], m)]['d'][1]
        else:
            return grille[pos]['g'][1]







def colorer_mur(t, ep):
    if ep == 1:
        t.color("red")
    elif ep == 2:
        t.color("lime")
    elif ep == 3:
        t.color("skyblue")
    elif ep == 4:
        t.color("blue")
    elif ep == 5:
        t.color("yellow")











    
def ajoute_coor(t, n, m, pas=100):
    t.color("red")
    t.up()
    t.goto(-750 + pas/2, 300 - pas/2)
    t.left(90)
    for l in range(1, n+1):
        for c in range(1, m+1):
            pos = "(" + str(l) + "," + str(c) + ")"
            t.write(pos , move=False,align='center',font=('Arial',8,'bold'))
            t.forward(pas)
        t.backward((m)*pas)
        t.right(90)
        t.forward(pas)
        t.left(90)


















def dessiner_grille(t, grille, n, m, pas=100, speed=5):
    
    t.speed(speed)
    t.shape("turtle")
    t.bgcolor("black")
    t.up()
    t.goto(-750, 300)
    t.down()

    #dessiner les murs horizontaux
    for l in range(1, n+2):
        for c in range(1, m+1):
            ep = ep_mur(grille, (l, c), 'h', n, m)
            colorer_mur(t, ep)
            t.width(6 + (ep-1)*4)
            t.forward(pas)
        t.up()
        t.backward(m*pas)
        t.right(90)
        t.forward(pas)
        t.left(90)
        t.down()

    t.up()
    t.right(90)
    t.backward((n+1)*pas)
    t.down()

    for c in range(1, m+2):
        for l in range(1, n+1):
            ep = ep_mur(grille, (l, c), 'v', n, m)
            colorer_mur(t, ep)
            t.width(6 + (ep-1)*4)
            t.forward(pas)
        t.up()
        t.backward(n*pas)
        t.left(90)
        t.forward(pas)
        t.right(90)
        t.down()

    ajoute_coor(t, n, m, pas)
    t.color("white")
    t.up()
    t.color("white")




def DesssinerPCC(t, PCC, Gr, pas, color, cout, speed=1,):
    t.speed(speed)
    t.up()
    t.goto(-750, 300)
    t.seth(0)
    for i in range(len(PCC) - 1):
        ep = 0
        x, y = 0, 0
        l1, c1 = PCC[i]
        l2, c2 = PCC[i+1]
        if l1 == l2 and c1 == c2 + 1:
            ep = Gr[PCC[i]]['g'][1]
            x = -750 + (PCC[i][1] - 1) * pas
            y = 300 - (PCC[i][0] - 1) * pas 
            t.width(6 + (ep-1)*4)
            t.seth(-90)
        elif l1 == l2 + 1 and c1 == c2:
            ep = Gr[PCC[i]]['h'][1]
            x = -750 + (PCC[i][1] - 1) * pas 
            y = 300 - (PCC[i][0] - 1) * pas
            t.width(6 + (ep-1)*4)
            t.seth(0)
        elif l1 == l2 and c1 == c2 - 1:
            ep = Gr[PCC[i]]['d'][1]
            x = pas -750 + (PCC[i][1] - 1) * pas
            y = 300 - (PCC[i][0] - 1) * pas
            t.width(6 + (ep-1)*4)
            t.seth(-90)
        elif l1 == l2 - 1 and c1 == c2:
            ep = Gr[PCC[i]]['b'][1]
            x = -750 + (PCC[i][1] - 1) * pas
            y = - pas + 300 - (PCC[i][0] - 1) * pas
            t.width(6 + (ep-1)*4)
            t.seth(0)
        t.goto(x, y)
        t.down()
        t.color(color)
        t.forward(pas/3)
        t.color("black")
        t.forward(pas/3)
        t.color(color)
        t.forward(pas/3)
        t.up()
    Ecrire_chemin_cout(t, PCC, cout)


def Ecrire_chemin_cout(t, PCC, cout):
    t.up()
    t.color("white")
    t.goto(-710, 350)
    t.write("Chemin : ", move=True, align='left', font=('Georgia', 15, 'bold'))
    for cel in PCC:
        text = str(cel) + "  "
        t.write(text , move=True,align='left',font=('Georgia',15,'bold'))
    t.up()
    t.goto(-710, 330)
    t.write("Cout : " + str(cout), move=True, align='left', font=('Georgia', 15, 'bold'))

def rid_t(t):
    '''éloigner la tortue de la grille'''
    t.up()
    t.goto(-750, 400)
    t.done()

#____________partie_tests___________________
# print( ep_mur(grille, (1, 5), 'v', 3, 4) )
# ajoute_coor(3, 4, 70)
# n, m = 3, 4
# Gr = Grille.creer_grille(n, m)
# dessiner_grille(Gr, n, m, 70)
#______________end_tests___________________




