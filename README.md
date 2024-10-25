# La Machine à Inventer des Mots

Ce projet utilise un modèle de trigramme pour générer des mots en français.

## Instructions

1. Exécutez `mots_trigrammes_count.py` pour créer la matrice des trigrammes, qui sera sauvegardée sous le nom `count.bin`.
2. Exécutez ensuite `mots_trigrammes_generate.py` pour générer des mots basés sur cette matrice. Les nouveaux mots seront enregistrés dans le fichier `output.txt`.

Le programme vérifie que les mots générés n'existent pas déjà dans le fichier `liste.de.mots.francais.frgut.txt`.
