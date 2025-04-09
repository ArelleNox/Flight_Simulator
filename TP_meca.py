import math as mt
import matplotlib.pyplot as plt

###FONCTION
#etape 1
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

#etape 2 & 4
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

    rotation_combinée = produit_matrice(matriceRZ, matriceRY)
    rotation_combinée2 = produit_matrice(rotation_combinée, matriceRX)

    return rotation_combinée2


#etape 3
def produit_matrice(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Le nombre de colonne de A doit être égale au nombre de ligne de B.")
    
    C = [[0 for i in range(len(B[0]))] for j in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    print("A x B = ", C)
    
    return C

#etape 5
def position_camera(P):
    position = [P[0][3], P[1][3], P[2][3]]
    print("\nPosition caméra :", position)
    return position

def dessiner_axes(ax, P, etiquette, couleur):
    origine = [P[0][3], P[1][3], P[2][3]]
    x_dir = [P[0][0], P[1][0], P[2][0]]
    y_dir = [P[0][1], P[1][1], P[2][1]]
    z_dir = [P[0][2], P[1][2], P[2][2]]

    ax.quiver(*origine, *x_dir, color=couleur, arrow_length_ratio=0.1)
    ax.quiver(*origine, *y_dir, color=couleur, arrow_length_ratio=0.1)
    ax.quiver(*origine, *z_dir, color=couleur, arrow_length_ratio=0.1)

    ax.text(*(origine[i] + x_dir[i] for i in range(3)), f"{etiquette}_x")
    ax.text(*(origine[i] + y_dir[i] for i in range(3)), f"{etiquette}_y")
    ax.text(*(origine[i] + z_dir[i] for i in range(3)), f"{etiquette}_z")

def afficher_world_et_camera(coordonnees_world, C, Pw):
    print("\n--- Affichage 3D ---")
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    world_x, world_y, world_z = coordonnees_world
    ax.scatter(world_x, world_y, world_z, c='b', marker='o',label='Coordonnées world', s=54)

    pos_cam = position_camera(C)
    ax.scatter(*pos_cam, c='r', marker='^', label='Position Caméra', s=54)

    ax.scatter(*Pw, c='b', marker='^', label='Position Pw avion ennemi', s=54)
    print("Position avion ennemi Pw :", Pw)

    dessiner_axes(ax, C, "C", couleur="red")
    dessiner_axes(ax, [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], "W",couleur="blue")

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_zlim(-4, 4)
    ax.legend()
    plt.show() 

def determinant_matrice(M):
    if len(M) != len(M[0]):
        raise ValueError("La matrice doit être carrée.")
    if len(M) == 0:
        raise ValueError("La matrice ne peut pas être vide.")
    
    if len(M) == 1 and len(M[0]) == 1:
        return M[0][0]
    elif len(M) == 2 and len(M[0]) == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]

    det = 0
    for j in range(len(M[0])):
        # Create the submatrix by excluding the i-th row and j-th column
        submatrix = [row[:j] + row[j+1:] for k, row in enumerate(M) if k != 0]
        det += ((-1) ** j) * M[0][j] * determinant_matrice(submatrix)
    
    print("Determinant de la matrice de passage :", det)
    return det

#etape 6
def inverse_matrice(M):
    if len(M) != len(M[0]):
        raise ValueError("La matrice doit être carrée.")
    if len(M) == 0:
        raise ValueError("La matrice ne peut pas être vide.")
    
    det = determinant_matrice(M)
    if det == 0:
        raise ValueError("La matrice est non inversible (déterminant nul).")
    
    n = len(M)
    



###INTERFACE

print("Matrice de translation")
T = [3,4,2]
matrice_translation(T)
print(" ")

print("Matrice de rotation")
R = ([mt.pi, mt.pi/2, mt.pi/4])
matrice_rotation(R)

print("Produit de matrice")
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

print("Matrice de passage")
matrice_de_passage = produit_matrice(matrice_translation(T), matrice_rotation(R))
print(" ")


M = matrice_de_passage
determinant_matrice(M)
print(" ")

print("Inverse de la matrice de passage")
inverse_matrice(M)
print(" ")

print("Position de la caméra")
origine_world = (0, 0, 0)
Pw = [[2],[2],[1]]
afficher_world_et_camera(origine_world, matrice_de_passage, Pw)

