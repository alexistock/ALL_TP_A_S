
L1 = [2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7]
compteur = 0 
frequent = 0
iteration = 0
for i in range (len(L1)):
    for j in range ((len(L1))):
        if L1[i] == L1[j]:
            compteur  += 1
    if compteur >= iteration:
        if compteur == iteration: 
            if  frequent < L1[i]:
                iteration = compteur
                frequent = L1[i]
        else:
            iteration = compteur
            frequent = L1[i]
    compteur = 0


print("Le nombre le plus frequent dans la liste est le : {} ({} x)".format(frequent, iteration))
tab = [0] *(max(L1) + 1)
for element in L1:
    tab[element] = L1.count(element)

element_freq= tab.index(max(tab))
iterationc = max(tab)
print("Le nombre le plus frequent dans la liste est le : {} ({} x)".format(element_freq, iterationc))
