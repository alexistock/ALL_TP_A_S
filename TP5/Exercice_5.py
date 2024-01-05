heure_travailler = int(input("Entrer le nombre d'heure travailler : "))
Salaire_horaire = float(input("Entrer votre salaire horaire : "))
Salaire = 0
if heure_travailler <= 160: 
    Salaire = heure_travailler * Salaire_horaire
if heure_travailler > 160 and heure_travailler <= 200:
    heure_travailler -= 160 
    Salaire =  (Salaire_horaire * 160) + (Salaire_horaire * heure_travailler * 1.25)
if heure_travailler > 200: 
    heure_travailler -= 200
    Salaire =  (Salaire_horaire * 160) + (Salaire_horaire * 40 * 1.25) + (Salaire_horaire * heure_travailler * 1.50)
print (Salaire)
