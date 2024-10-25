# -*- coding: utf-8 -*-
# mots_trigrammes_generate.py
# Génère des mots en utilisant la matrice de transition de trigrammes

import numpy as np
from numpy.random import choice
import codecs

# Charger le fichier de mots français dans une liste pour vérifier les doublons
filepath = "liste.de.mots.francais.frgut.txt"
dico = set()
with codecs.open(filepath, "r", "utf-8") as lines:
    for line in lines:
        dico.add(line.strip())

# Chargement et normalisation de la matrice de transition des trigrammes
count = np.fromfile("count.bin", dtype="int32").reshape((256, 256, 256))
s = count.sum(axis=2)

# Correction : éviter les divisions par zéro et les lignes de transition nulles
s[s == 0] = 1  # Empêche la division par zéro
p = count / s[:, :, None]  # Normalisation de probabilité
p[np.isnan(p)] = 0  # Remplace NaN par zéro

# Vérification et correction des probabilités
for i in range(256):
    for j in range(256):
        if not np.isclose(p[i, j, :].sum(), 1.0):
            # Redistribution uniforme si la somme est trop éloignée de 1
            p[i, j, :] = 1.0 / 256

# Génération de nouveaux mots
outfile = "output.txt"
with codecs.open(outfile, "w", "utf-8") as f:
    target_length = 50000  # Nombre de mots à générer par longueur cible
    for TGT in range(4, 17):  # Longueur de mot cible de 4 à 10
        total_generated = 0
        while total_generated < target_length:
            i, j = 0, 0
            word = ""
            # Génération d'un mot de longueur spécifique
            while True:
                k = choice(range(256), p=p[i, j, :])
                if k == 10:  # Arrêter si caractère de fin de ligne
                    break
                word += chr(k)
                if len(word) == TGT:
                    break
                i, j = j, k
            if word and word not in dico:  # Vérifie si le mot est nouveau
                f.write(word + "\n")
                total_generated += 1
                print(f"Mot généré : {word}")

print("Génération de mots terminée et sauvegardée dans 'output.txt'")




