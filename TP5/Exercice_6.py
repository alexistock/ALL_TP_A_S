T = "hgjcsqghjigujgzuigeuguwagon Le wagon bleu est rapide. 0 "
i = 0
phrase_rechercher = str(input("entreter la phrase que vous rechercher: "))
voyelle = 0
lst_voyelle=["a","e","i","o","u","y"]
phrase_présente = True
compteur =0
boucleOn = True
while T[i] != "0": 
    i += 1
    if T[i] in lst_voyelle:
        voyelle += 1
    if T[i] == phrase_rechercher[0]:
        while boucleOn == True:
            if T[compteur+i] != phrase_rechercher[compteur]:
                phrase_présente = False
            if phrase_rechercher[compteur] != ".":
                boucleOn = False


print (f"Il y à {round(voyelle/(i-1)*100,1)}%  de voyelles contenues dans la chaîne de caractères")
if phrase_présente:
    print("la phrase est présente")
else:
    print("la phrase n'est pas présente")

