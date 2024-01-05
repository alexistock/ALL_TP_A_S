Palindrome = str(input("Entrez un mot ou une phrase : "))
Palindrome = Palindrome.lower()
droite = 0
gauche = len(Palindrome)
Est_un_Palindrome = True
while Palindrome[droite] != Palindrome[gauche] or Est_un_Palindrome:
    while not Palindrome[droite].isalpha() or not Palindrome[droite].isalpha():
        if not Palindrome[droite].isalpha():
            droite += 1
        if not Palindrome[gauche].isalpha():
            gauche -= 1
    if Palindrome[droite] != Palindrome[gauche]:
        Est_un_Palindrome = False
    droite +=1
    gauche -= 1
if Est_un_Palindrome:
    print("C'est un palindrome")
else:
    print("Ce n'est pas un palindrome")