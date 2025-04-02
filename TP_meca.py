import math as mt
import matplotlib.pyplot as plt

###FONCTION
def matrice_translation(vecteur_translation):
    if len (vecteur_translation) != 3:
        raise ValueError("Le vecteur de translation doit contenire 3 element (a, b, c).")
    
    a, b, c= vecteur_translation
    
    matriceT = [
        [1, 0, 0, a],
        [0, 1, 0, b],
        [0, 0, 1, c],
        [0, 0, 0, 1]
    ]

    for row in matriceT:
        print(row)
    
    return matriceT


    # print("n\--- Matrice de translation---")
    # print("T=", matriceT)
    # return matriceT


###INTERFACE