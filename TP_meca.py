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
        print("n\--- Matrice de translation---")
        print(row)
    
    return matriceT


    


def matrice_rotation(vecteur_rotation):
    if len (vecteur_rotation) != 3:
        raise ValueError("Le vecteur de rotation doit contenire 3 element (x, y, z).")
    
    x, y, z= vecteur_rotation

    matriceRX = [
            [1, 0, 0, 0],
            [0, mt.cos(x), -mt.sin(x), 0],
            [0, mt.sin(x), mt.cos(x), 0],
            [0, 0, 0, 1]
        ]

    matriceRY = [
            [mt.cos(y), 0, mt.sin(y), 0],
            [0, 1, 0, 0],
            [-mt.sin(y), 0, mt.cos(y), 0],
            [0, 0, 0, 1]
        ]

    matriceRZ = [
            [mt.cos(z), -mt.sin(z), 0, 0],
            [mt.sin(z), mt.cos(z), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]

    # print("n\--- Matrice de rotation---")
    # for row in matriceRX and matriceRY and matriceRZ:
    #     print(row)
    
    # return matriceRX, matriceRY, matriceRZ


    print("n\--- Matrice de rotation---")
    print("n\Matrice de Rx=", matriceRX)
    print("n\Matrice de Ry=", matriceRY)
    print("n\Matrice de Rz=", matriceRZ)

matrice_translation([3, 4, 2])
matrice_rotation([mt.pi, mt.pi/2, mt.pi/4])
###INTERFACE