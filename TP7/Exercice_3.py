import sys
import os
def recherche(nom_dos):
    liste = os.listdir(nom_dos)
    fichier =[]
    dossier = []
    chemin_dossier  = []
    antislach = " \ "
    antislach = antislach.replace(" ","")
    for i in range(len(liste)):
        if os.path.isfile(nom_dos+antislach+liste[i]): # renvoie vrai si ‘nom’ est un fichier standard.
            fichier.append(liste[i])
        if os.path.isdir(nom_dos+antislach+liste[i]): #renvoie vrai si ‘nom’ est un répertoire.
            dossier.append(liste[i])
            chemin_dossier.append(nom_dos+antislach+liste[i])
    return fichier, dossier, chemin_dossier

def aide (erreure):
    if erreure == 1:
        print(f"Pas assez d’arguments pour le script {sys.argv[0]}")
    if erreure == 2:
        print(f"Le dossier n'existe pas{sys.argv[0]}")
    print("Pour utiliser se script Passer en argument un fichier existant\nSe qui permetera de pouvoir afficher les fichier contenu dans se fichier")

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        aide(1)
    if not(os.path.exists(sys.argv[1])):
        aide(2)
    else:
        compteur = 0
        fichier, dossier, chemin_dossier  = recherche(sys.argv[1])
        print(fichier)
        print(dossier)
        while len(chemin_dossier) != 0:
                
                fichier, dossier, nouveau_chemin_dossier = recherche(chemin_dossier[compteur])
                del(chemin_dossier[0])
                chemin_dossier+= nouveau_chemin_dossier
                print(fichier)
                if len(dossier)!= 0:
                    print(dossier)
                compteur += 1
                