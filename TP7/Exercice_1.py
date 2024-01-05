import sys
if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print(f"Pas assez d’arguments pour le script {sys.argv[0]}")
    elif len(sys.argv) > 2:
        for elt in sys.argv: # pour chaque élément de la liste sys.argv
            print(elt)


