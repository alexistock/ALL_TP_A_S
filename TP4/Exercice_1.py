table = float(input("Vous cherchez la table de multiplication de quel nombre ? "))
lst = []
for i in range (10):
    lst.append(round((table*i),1))
for i in range ((len(lst))):
    print("{} * {} = {}".format(table, i, lst[i]) )