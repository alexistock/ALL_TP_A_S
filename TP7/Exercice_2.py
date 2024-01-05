import sys
import os
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
        contenu =os.listdir(sys.argv[1])
        for i in range (len(contenu)):
            print(contenu[i])