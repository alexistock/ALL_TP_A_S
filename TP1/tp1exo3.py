jour = int(input("Saisir les jours: "))
heure = int(input("Saisir les heures: "))
minute = int(input("Saisir les minutes: "))
resultat_en_minutes = (jour * 24 * 64 + heure * 60 + minute)
print("le nombres de minutes ecoulé depuis le deubut de l année est de {} minutes".format(resultat_en_minutes))


