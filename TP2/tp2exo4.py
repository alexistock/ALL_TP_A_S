BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nombre_conviees = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))
print("Pour faire une fondue fribourgeoise pour 3 personnes, il vous faut :")
fromage = fromage * nombre_conviees / BASE
eau = eau * nombre_conviees / BASE
ail= ail * nombre_conviees / BASE
pain = pain * nombre_conviees / BASE
print('- {} gr de fromage'.format(fromage))
print('- {} dl d eau'.format(eau))
print('- {} gousse(s) d ail'.format(ail))
print('- {} gr de pain'.format(pain))


