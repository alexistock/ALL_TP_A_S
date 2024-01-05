produit_scal = 0
nMax = 10
v1 , v2 = [], []
n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ? "))
while n < 1  or n > 10:
    print('La taille effective des vecteurs doit étre compris entre 1 et 10')
    n = float(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ?"))
print('\nSaisie du premier vecteur :')
for i in range(n):
    v1.append(float(input("v1[{}] = ".format(i))))
print('\nSaisie du second vecteur :')
for i in range(n):
    v2.append(float(input("v2[{}] = ".format(i))))
for i in range (n):
    produit_scal += v1[i] * v2[i]
print("\nLe produit scalaire de v1 par v2 vaut {}".format(produit_scal))
