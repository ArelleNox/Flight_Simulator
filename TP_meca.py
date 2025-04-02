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


    print("--- Matrice de rotation---")
    print("Matrice de Rx=", matriceRX)
    print("Matrice de Ry=", matriceRY)
    print("Matrice de Rz=", matriceRZ)


def produit_matrice(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Le nombre de colonne de A doit être égale au nombre de ligne de B.")
    
    C = [[0 for i in range(len(B[0]))] for j in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    print("\n--- Produit de matrices ---")
    print("A x B = ", C)
    
    return C


###INTERFACE

print("Matrice de translation")
T = [3,4,2]
matrice_translation(T)
print(" ")

R = ([mt.pi, mt.pi/2, mt.pi/4])
matrice_rotation(R)

A = [
[1, 2, 0, 3],
[0, 0, 0, 2],
[1, 2, 1, 5],
[0, 0, 1, 1]
]
B = [
[0, 0, 3, 0],
[0, 1, 0, 1],
[4, 1, 3, 0],
[1, 2, 1, 0]
]
produit_matrice(A,B)
print(" ")