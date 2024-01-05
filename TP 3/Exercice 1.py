def a():
    n = int(input("choisiser un nombre entier"))
    resultat = 0
    for i in range(n):
        resultat += i+1
        print(resultat)

"calcul_affichage()"
def b():
    valeur =int(input("entrer la valeur 100 pour arreter la bocule: "))
    while valeur != 100:
        valeur =int(input("entrer la valeur 100 pour arreter la bocule: "))
    print("boucle arréter")

def c():
    lst = []
    lst1 = []
    lst2 =[]
    lst3 = []
    for i in range (10):
        lst.append( int(input("entre un nombre enbtre 1 et 20: ")))
    for j in range( 10):
        if lst[j] < 10:
            lst1.append(lst[j])
        elif lst[j] >= 10 and lst[j] < 15:
            lst2.append(lst[j])
        else:
            lst3.append(lst[j])
    print("Le nombre de valeurs inférieur strictement à 10: {}".format(lst1))
    print("Le nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15: {}".format(lst2))
    print("Le nombre de valeurs supérieur ou égale à 15: {}".format(lst3))

def d():
    X = int(input("Entre votre nombre"))
    N = 0
    somme = 0
    while somme <= X:
        N += 1
        somme += N
        print("somme")
    print("la somme s'arrete a {}".format(N))

a()
b()
c()
d()