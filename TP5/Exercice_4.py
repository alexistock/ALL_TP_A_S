
somme = int(input("Entrer votre somme d'argent"))
somme_copy = somme
billet100 = somme // 100 
somme = somme % 100
billet50 = somme // 50
somme = somme % 50
billet10 = somme // 10
somme = somme % 10
piéce2 = somme // 2
somme = somme % 2
piéce1 = somme 
print(f" {somme_copy} euros, c’est donc {billet100}billets de 100, {billet50} de 50, {billet10} de 10, {piéce2} pièces de 2 et {piéce1} pièce 1. ")

