def reinitialiser_fichier(nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        fichier.truncate(0)

# Utilisation de la fonction pour réinitialiser le fichier "mots.txt"
reinitialiser_fichier("mots.txt")
