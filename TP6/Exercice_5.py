Palindrome = str(input("Entrer un mots ou  une phrase: "))
def nettoyage(Palindrome):
    Palindrome = Palindrome.lower()
    res = Palindrome
    for i in range(len(Palindrome)):
        if Palindrome[i] == "!" or "?" or "." or "," or "'" :
            res = res.replace(Palindrome[i],"")
        if Palindrome[i] == 'é' or  'è' or 'ê' or 'ẽ':
            res = res.replace(Palindrome[i],'e') 
        if Palindrome[i] == 'ç':
            res = res.replace(Palindrome[i],'c') 
        if Palindrome[i] == 'à'or 'â' or 'ã':
            res = res.replace(Palindrome[i],'a') 
    res = res.replace(" ","")
    return (res)
print(nettoyage(Palindrome))