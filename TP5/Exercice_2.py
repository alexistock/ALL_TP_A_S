compteur_coef = 0
moyenne = 0
for i in range (5):
    NoteEtCoef = str(input('Veuillez entrer la note du module 1 et le coefficientcorrespondant : '))
    NoteEtCoef = NoteEtCoef.split(" ")
    moyenne += float(NoteEtCoef[0]) * int(NoteEtCoef[1])
    compteur_coef += int(NoteEtCoef[1])
print(moyenne/compteur_coef)
