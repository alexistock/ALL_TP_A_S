nom = "toto"
prenom = "tata"
math= 15.3
anglais = 19.1
info = 15.3
promotion = 2023
moy = math + anglais + info
moyenne = moy/3
print (type(nom))
print (type(prenom))
print (type(math))
print (type(anglais))
print (type(info))
print (type(promotion))
print("l'etudiant {} {} de la promotion {} a une moyenne de {}" .format(nom,prenom,promotion,moyenne))