# TNSI_projet_2.1
Projet 2.1 de NSI terminale



Le jeu pyxel consiste a tuer les ennemis.
C'est un jeu 2D avec possibilite de faire du ray tracing



# informations specifiques
parametres de la map virtuelles pour les hitbox pour faciliter les calculs
rien = 0,
mur = 1
joueur = 2
monstre = 3"nbr
objet = 4
joueur + monstre = 5"nbr
balle = 6
balle + joueur = 7
balle + monstres = 8"nbr
objet + monstre = 9"nbr



# problemes rencontres
Dans la 2e refonte totale du calcul de hitbox.
J'ai assigné les positions des objets et entitees dans mon dictionnaire a des positions de variables sortantes d'une boucle for et qui par consequent sont deplaces de 15px de cote (pas 16 a cause d'une erreur de boucle)
et donc des entitees se sont retrouvees hors de la map leurs positions ont etes calculées hors de la map elle ne pouvaient pas bouger mais elles etaient toujours hors de la map. donc quand on les assignait ou retirait de la map les positions se retrouvaient hors de la map

Cette petite erreur d'assignation m'a coute 4h voir un peu plus