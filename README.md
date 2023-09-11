# FOX AND GEESE - Readme

## 1. Contexte du projet

La société "Puzzle Games" souhaite adapter le jeu "Fox And Geese" en version numérique. Elle cherche un sous-traitant pour développer une version bureau de ce jeu sur les trois principaux systèmes d'exploitation actuels : Linux, Windows et Mac OS X. Le contrat concerne la conception et le développement d'un jeu de stratégie combinatoire abstrait, incluant un nouveau thème graphique, une gestion complète du jeu à la souris et plusieurs fonctionnalités.


## 2. Description du projet

### 2.1 - Le jeu

Le "Fox And Geese" est un jeu de stratégie combinatoire abstrait pour deux joueurs, où chacun doit atteindre le côté opposé du plateau avant son adversaire en utilisant les pions et les barrières pour bloquer l'avancée de l'autre joueur.

Des ressources complètes sur le jeu et ses règles sont disponibles sur GitHub.


### 2.2 - Fonctionnalités générales à implémenter
Le projet devra inclure les fonctionnalités suivantes :

- Redéfinition de l'univers graphique<br>
- Gestion complète du jeu à la souris<br>
- Choix de plusieurs configurations :<br>
- Quatre tailles de plateaux : 5x5, 7x7, 9x9, 11x11<br>
- Choix du nombre de barrières : multiples de 4 entre 4 et 40. Restreindre les possibilités en fonction de la taille du plateau.<br>
- Les valeurs par défaut sont un plateau de 9x9 et un nombre de barrières égal à 20.<br>
- Choix du nombre de joueurs<br>
- Choix du type de jeu (en réseau ou non)<br>
- Une version du jeu où les deux ou quatre joueurs s'affrontent sur le même ordinateur<br>
- Une version du jeu où les deux ou quatre joueurs s'affrontent en réseau sur deux ou quatre machines différentes<br>
- Une version du jeu où un joueur humain joue contre un ordinateur, ce dernier choisissant ses coups de manière aléatoire<br>
- Possibilité de rejouer<br>


## 3. Le rendu

Le rendu du projet est une archive au format "zip" contenant :
- Le code source
- Les fichiers annexes (sons, images, etc.)
- La documentation technique
- Le manuel du jeu

La documentation technique contient :

- Justification du choix du langage et de la librairie graphique
- Description précise des structures de données
- Présentation des algorithmes de gestion du déplacement des pions
- Présentation des algorithmes de gestion de la pose des barrières
- Explication du procédé utilisé pour faire communiquer plusieurs ordinateurs lors du jeu en réseau

- Le manuel du jeu contient :

- Un rappel des règles du jeu
- Comment lancer le jeu
- Comment y jouer


## 4. Auteurs

Cureau Melvin.


## 5. Licence

Ce projet est sous licence MIT. Voir le fichier LICENCE pour plus de détails.
