from time import sleep
def avec_for():
    n = int(input("saisir un nombre entier n positif: "))
    for i in range(n+1):
        print(n -i)
        sleep(0.5)
def avec_while():
    n = int(input("saisir un nombre entier n positif: "))
    while n !=0:
        print(n)
        n = n-1
        sleep(0.5)
avec_for()
avec_while()