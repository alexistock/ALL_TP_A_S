def facto():
    n = int(input("donnée la factorielle d'un entier n: "))
    choix = 0
    while choix != 2 or choix !=1:
        choix  = int(input("entré 1 pour avec boucle for et 2 pour boucle while"))
    resultat = 0
    compteur = 0
    if choix == 1:
        for i in range (n):
            resultat += i+1
            print(resultat)
    if choix == 2:
        while compteur != n:
            compteur +=1
            resultat += compteur 
            print(resultat)