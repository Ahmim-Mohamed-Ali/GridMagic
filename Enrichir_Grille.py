import Grille as g
import PlusCoursChemin as pcc
import turtle as t
import DessinerGrille






t.bgcolor("black")



def enrichir(grille, PCC):
    for i in range(len(PCC) - 1):
        l, c = PCC[i]
        l_, c_ = PCC[i+1]
        if l == l_ and c == c_ + 1:
            grille[PCC[i]]['g'].append(True)
            grille[PCC[i+1]]['d'].append(True)
        elif l == l_ and c == c_ - 1:
            grille[PCC[i]]['d'].append(True)
            grille[PCC[i+1]]['g'].append(True)
        elif l == l_ + 1 and c == c_:
            grille[PCC[i]]['h'].append(True)
            grille[PCC[i+1]]['b'].append(True)
        elif l == l_ - 1 and c == c_:
            grille[PCC[i]]['b'].append(True)
            grille[PCC[i+1]]['h'].append(True)
    


def general(mur, pas, cel):
    angle, pos = 0, ''
    x, y = 0, 0
    if mur == 'g':
        pos = 'd'
        angle = -90
        x = -750 + (cel[1] - 1) * pas
        y = 300 - (cel[0] - 1) * pas 
    elif mur == 'd':
        pos ='g'
        angle = -90
        x = pas -750 + (cel[1] - 1) * pas
        y = 300 - (cel[0] - 1) * pas
    elif mur == 'h':
        pos ='b'
        angle = 0
        x = -750 + (cel[1] - 1) * pas 
        y = 300 - (cel[0] - 1) * pas
    else :
        pos ='h'
        angle = 0
        x = -750 + (cel[1] - 1) * pas
        y = - pas + 300 - (cel[0] - 1) * pas
    return pos, angle, x, y

#ceci va servir pour repondre à la question b) de la partie 3
def adapter_dessin(t, grille, color = "white", pas = 100):
    t.color(color)
    t.up()
    t.goto(-750, 300)
    t.seth(0)
    for cel in grille:
        for mur in grille[cel]:
            if len(grille[cel][mur]) == 3:

                # print("general : ", general(mur, pas, cel))
                pos, angle, x, y = general(mur, pas, cel)

                cel_rep = grille[cel][mur][0]
                del(grille[cel_rep][pos][2])
                ep = grille[cel][mur][1]

                t.width(6 + (ep-1)*4)
                t.seth(angle)

                t.goto(x, y)
                t.down()
                t.forward(pas/3)
                t.color("black")
                t.forward(pas/3)
                t.color(color)
                t.forward(pas/3)
                t.up()



#__________APPLICATION______________
n, m = 3, 4
gpt = g.creer_grille(n, m)
p_c_c = pcc.plus_court_chemin(gpt, n, m)[0]
enrichir(gpt, p_c_c)

DessinerGrille.dessiner_grille(t, gpt, n, m)
adapter_dessin(t, gpt)


t.done()