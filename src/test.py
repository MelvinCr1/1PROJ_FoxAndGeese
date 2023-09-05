from tkinter import Tk, Canvas

# Définition de la matrice
matrix = [
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0]
]

# Taille des cellules de la matrice
cell_size = 30

# Création de la fenêtre Tkinter
root = Tk()

# Calcul de la taille du canevas
canvas_width = len(matrix[0]) * cell_size
canvas_height = len(matrix) * cell_size

# Création du canevas
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Parcours de la matrice et dessin des points ovales et des lignes diagonales
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            x = j * cell_size + cell_size // 2
            y = i * cell_size + cell_size // 2
            canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black")

            if i > 0 and j > 0 and matrix[i - 1][j - 1] == 1:  # Vérification du point en haut à gauche
                canvas.create_line(x, y, x - cell_size, y - cell_size)

            if i > 0 and j < len(matrix[i]) - 1 and matrix[i - 1][j + 1] == 1:  # Vérification du point en haut à droite
                canvas.create_line(x, y, x + cell_size, y - cell_size)

            if i < len(matrix) - 1 and j > 0 and matrix[i + 1][j - 1] == 1:  # Vérification du point en bas à gauche
                canvas.create_line(x, y, x - cell_size, y + cell_size)

            if i < len(matrix) - 1 and j < len(matrix[i]) - 1 and matrix[i + 1][
                j + 1] == 1:  # Vérification du point en bas à droite
                canvas.create_line(x, y, x + cell_size, y + cell_size)

# Lancement de la boucle principale Tkinter
root.mainloop()
