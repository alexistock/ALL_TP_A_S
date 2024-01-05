# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
# déclaration d’une liste vide qui va contenir autant de notes que
notes = []
print("")
for i in  range(nombreEtudiants):
    note=float(input(" Note etudiant {} : ".format(i)))
    if note > 20 or note < 0:
        while note > 20 or note < 0:
            notes=float(input("Note etudiant {} : ".format(i)))
    notes.append(note)
for i in range (len(notes)):
    moyenne += notes[i]
moyenne = moyenne/len(notes)
print("Moyenne de classe : {} \n".format(moyenne))
print("Numéro de l’Etudiant | note | ecart a la moyenne \n")
for i in range(len(notes)):
    print("{} | {} | {}".format(i , notes[i], notes[i] - moyenne))



