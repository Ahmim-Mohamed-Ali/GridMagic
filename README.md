# MagicGrid


# Descripiton Du Projet
Bienvenue dans le projet Magic Grid ! Ce projet vise à modéliser des objets réels à l'aide de structures de données appropriées, à employer diverses techniques de programmation et à utiliser des algorithmes célèbres tels que les algorithmes de Bellman-Ford et de Dijkstra pour résoudre des problèmes du monde réel.

L'objectif principal de ce projet est de naviguer à travers une grille complexe composée de cellules avec des longueurs de murs variables. Le but est de partir de la cellule en haut à gauche et d'atteindre la cellule en bas à droite en détruisant les murs entre les cellules adjacentes. Le défi consiste à trouver la combinaison optimale de cellules pour minimiser l'effort nécessaire à la destruction des murs, en garantissant que les murs soient aussi minces que possible.

Pour représenter la grille, nous utilisons un graphique comme structure de données. En utilisant l'algorithme de Dijkstra, nous pouvons trouver le chemin le plus court possible à travers le graphique, ce qui nous permet de parcourir la grille efficacement. De plus, l'algorithme de Bellman-Ford est utilisé pour garantir que le chemin choisi est non seulement le plus court mais également le plus optimal.

En prime, nous avons implémenté un algorithme heuristique pour trouver un chemin localement optimal dans un laps de temps relativement court. Cet algorithme heuristique propose une approche alternative pour trouver un chemin quasi optimal.

# Technologies Utilisées
Python : Nous avons utilisé Python comme langage de programmation pour l'ensemble du projet, en tirant parti de sa simplicité et de sa polyvalence.

Turtle.py : la bibliothèque Turtle de Python a été utilisée pour dessiner la grille et visualiser les chemins, ce qui facilite la compréhension de la solution.

# Getting Started
Pour démarrer le projet Magic Grid, suivez ces étapes :

Clonez le référentiel du projet depuis GitHub : git clone (https://github.com/Ahmim-Mohamed-Ali/GridMagic/tree/main)
Installez les dépendances requises. Assurez-vous que Python est installé sur votre ordinateur. pip installer la tortue
Accédez au répertoire du projet : cd The-Magic-Grid
Exécutez le fichier Python principal pour exécuter le programme de modélisation de grille : python Main.py
Une fois le programme exécuté, vous pouvez interagir avec l'application de modélisation de grille via l'interface utilisateur graphique. 
Suivez les instructions affichées à l'écran pour :
Spécifiez les dimensions de la grille et les longueurs des murs dans chaque cellule.
Visualisez la grille et le chemin actuel.

