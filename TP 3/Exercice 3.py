from random import randint
def nombre_mystère():
    nombre_mystère = randint(1,100)
    compteur = 1
    valeur = int(input("Donner un nombre entre 1 et 100: "))
    while valeur != nombre_mystère:
        compteur +=  1
        if valeur > nombre_mystère:
            valeur = int(input("le nombre mystère est plus petit, rentrer un nouveau nombre"))
        else: 
            valeur = int(input("le nombre mystère est plus grands, rentrer un nouveau nombre"))
    print("Bravo vous avez trouvez le nombre mystère {} en {} coups".format(nombre_mystère, compteur))

nombre_mystère()