Lst1 = [0, 1, 2]
def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst
Lst2 = ajouter_elt(Lst1, len(Lst1))

print(Lst1, type(Lst1), id(Lst1))
print(Lst2, type(Lst2), id(Lst2))
#c on remarque que les deux variable on le meme contenu, type et  identifiant