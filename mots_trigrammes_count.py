# -*- coding: utf-8 -*-
# mots_trigrammes_count.py
# Compte l'occurrence des trigrammes de caractères ASCII dans un fichier texte

import numpy as np
import codecs

# Chemin vers le fichier de mots français
filepath = "liste.de.mots.francais.frgut.txt"
# Crée une matrice 3D pour stocker les comptes de trigrammes
count = np.zeros((256, 256, 256), dtype='int32')

# Lecture et comptage des trigrammes dans le fichier de mots
with codecs.open(filepath, "r", "utf-8") as lines:
    for line in lines:
        i, j = 0, 0
        for k in [ord(c) for c in line.strip()]:  # Ignore les espaces blancs
            count[i, j, k] += 1
            i, j = j, k

# Sauvegarde de la matrice des comptes dans un fichier binaire
count.tofile("count.bin")

print("Comptage des trigrammes terminé et sauvegardé dans 'count.bin'")
