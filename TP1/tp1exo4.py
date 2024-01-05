minutes_moi = int(input("Saisir les minutes ecouler depuis le debut du mois :"))
jour = minutes_moi // (24 * 60)
minutes_moi = minutes_moi % (24 * 60)
heure =  minutes_moi // 60
minute = minutes_moi % 60
print("jour:{} ,heure: {}, minute : {}" .format(jour, heure, minute))
                  
