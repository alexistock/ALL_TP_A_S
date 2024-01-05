from random import randint
nombre = randint(0,100)
if nombre < 100*(2/3):
    print("Pile !")
else:
    print("Face !")