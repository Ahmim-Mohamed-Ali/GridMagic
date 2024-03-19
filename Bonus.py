import Grille
import turtle as t
import DessinerGrille as DG
import PlusCoursChemin as PCC
import Enrichir_Grille as enrichir




def efficace_pas_opti(grille, n, m):
    Chemin_dir = [(1, 1)]
    coût_dir = 0
    Chemin_indir = [(n, m)]
    coût_indir = 0
    fin = False

    #chemin loc_opt_dir
    while not fin:
        l, c = Chemin_dir[-1]
        if l == n and c == m:
            fin = True
        elif l == n:
            #aller à droite
            Chemin_dir.append( (l, c+1) )
            coût_dir += grille[(l, c)]['d'][1]
        elif c == m:
            #aller en bas
            Chemin_dir.append( (l+1, c) )
            coût_dir += grille[(l, c)]['b'][1]
        else:
            if grille[(l, c)]['d'][1] < grille[(l, c)]['b'][1]:
                Chemin_dir.append( grille[(l, c)]['d'][0] )
                coût_dir += grille[(l, c)]['d'][1]
            else:
                Chemin_dir.append( grille[(l, c)]['b'][0] )
                coût_dir += grille[(l, c)]['b'][1]

    fin = False
    #chemin loc_opt_indir
    while not fin:
        l, c = Chemin_indir[-1]
        if l == 1 and c == 1:
            fin = True
        elif l == 1:
            #aller à gauche
            Chemin_indir.append( (l, c-1) )
            coût_indir += grille[(l, c)]['g'][1]
        elif c == 1:
            #aller en haut
            Chemin_indir.append( (l-1, c) )
            coût_indir += grille[(l, c)]['h'][1]
        else:
            if grille[(l, c)]['g'][1] < grille[(l, c)]['h'][1]:
                Chemin_indir.append( grille[(l, c)]['g'][0] )
                coût_indir += grille[(l, c)]['g'][1]
            else:
                Chemin_indir.append( grille[(l, c)]['h'][0] )
                coût_indir += grille[(l, c)]['h'][1]
    
    if coût_dir < coût_indir:
        return Chemin_dir, coût_dir
    else:
        return Chemin_indir, coût_indir


#______________________APPLICAITON_____________________
n, m = 8, 5
maGrille = Grille.creer_grille(n, m)
DG.dessiner_grille(t, maGrille, n, m, 70, 11)

pcc_bel, cout = PCC.plus_court_chemin(maGrille, n, m, 'bel')
pcc_djiks, cout2 = PCC.plus_court_chemin(maGrille, n, m, 'dij')
#DG.DesssinerPCC(t, pcc_bel, maGrille, 70, "white", cout, 11)
#DG.DesssinerPCC(t, pcc_djiks, maGrille, 70, "white", cout2, 11)
enrichir.enrichir(maGrille, pcc_djiks)
enrichir.adapter_dessin(t, maGrille)
pcc_non_opt, cout_non_opt = efficace_pas_opti(maGrille, n, m)
print(cout_non_opt)

DG.DesssinerPCC(t, pcc_non_opt, maGrille, 70, "gray", cout_non_opt, 11)

DG.rid_t(t)






t.done()