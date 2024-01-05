import random

## Fonction generer(nbr, vmin, vmax) pour générer un tableau de 'nbr'
def generer(nbr, vmin, vmax):
    lst = []
    for i in range(nbr):
        lst.append(random.randint(vmin, vmax))
    return lst
## comprises entre 'vmin' et 'vmax'

## Fonction combienInferieur(table, vseuil) pour compter le nombre de
def combienInferieur(table, vseuil):
    compteur = 0
    for i in range(len(table)):
        if table[i]< vseuil:
            compteur += 1
    return compteur
## d'un tableau 'table' inférieures à la valeur 'vseuil'
nb = int(input("Quel est le nombre de valeur que vous voulez générer ? : "))
vmin = int(input("Quel doit étre la valeur minimal des nombres que vous voulez generer ? :"))
vmax = int(input("Quel doit étre la valeur maximal des nombres que vous voulez generer ? :"))
print(f"Générer {nb} nombres entiers entre 0 et 100")
tab = generer(nb, vmin, vmax)
tab.sort()
print(tab)
seuil = ""
while seuil != "Oui" and seuil != "O" and seuil != "Non" and seuil != "N":
    seuil = str(input("vous voulez préciser le seuil"))
    if seuil != "Oui" or seuil != "O" or seuil != "Non" or seuil != "N":
        print("vous devez entrer entrer les valeurs Oui|O ou Non|N")
if seuil ==  "Oui" or seuil == "O":
    seuil = int(input("Entrer la valeur du Seuil"))
else:
    seuil = 30
total = combienInferieur(tab, seuil)
print(f"Il y en a {total} inférieurs à {seuil}")
