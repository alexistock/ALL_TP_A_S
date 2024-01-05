

date = "31062023"
correct = False
if len(date) == 8:

    jour = int(date[0:2])
    mois = int(date[2:4])
    annee = int(date[4:])
    
    if jour >= 1 and jour <= 31:
        if mois in [4, 6, 9, 11] and (jour < 1 or jour > 30):
            correct = False
        elif mois >= 1 and mois <= 12:
            if mois == 2:
                if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
                    if jour >= 1 or jour <= 29:
                        correct = True
                else:
                    if jour >= 1 or jour <= 28:
                        correct = True


if correct == True:
        print("Date correct")
else:
        print("Date incorect")

dates_a_verifier = ["32052024", "00052022", "29022022", "28022002", "31062023"]

