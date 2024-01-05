nombre_entier =int(input("Entrez un nombre entier: "))
if nombre_entier > 0:
    if nombre_entier % 2 == 0:
        print("Le nombre est positif et pair")
    else:
        print("Le nombre est positif et impair")
elif nombre_entier < 0:
    if nombre_entier % 2 == 0:
        print("Le nombre est négatif et pair")
    else:
        print("Le nombre est négatif et impair")
else:
    print("Le nombre est zéro (et il est pair")