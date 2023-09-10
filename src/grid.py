from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pygame.mixer

class GridSelection:
    def __init__(self):
        pygame.mixer.init()
        self.__clickSound = pygame.mixer.Sound("Click.wav")
        self.__backgroundMusic = pygame.mixer.Sound("Hello.mp3")
        self.__backgroundMusic.play(-1)
        self.__root = Tk()
        self.__root.title("Fox And Geese")
        self.__root.geometry("950x300")
        self.__root.resizable(width=False, height=False)
        self.__root.iconbitmap("img\logo.ico")
        self.__gridSizeValue = IntVar(value=1)

    # Chargement de l'image
        self.__setup1 = Image.open("img\setup1.png")
        self.__setup2 = Image.open("img\setup2.png")
        self.__setup3 = Image.open("img\setup3.png")
        self.__setup4 = Image.open("img\setup4.png")
        self.__setup5 = Image.open("img\setup5.png")
    # Redimensionnement de l'image
        self.__setup1 = self.__setup1.resize((150, 150))
        self.__setup2 = self.__setup2.resize((150, 150))
        self.__setup3 = self.__setup3.resize((150, 150))
        self.__setup4 = self.__setup4.resize((150, 150))
        self.__setup5 = self.__setup5.resize((150, 150))
    # Conversion en image Tkinter
        setup1 = ImageTk.PhotoImage(self.__setup1)
        setup2 = ImageTk.PhotoImage(self.__setup2)
        setup3 = ImageTk.PhotoImage(self.__setup3)
        setup4 = ImageTk.PhotoImage(self.__setup4)
        setup5 = ImageTk.PhotoImage(self.__setup5)

        self.__frame1 = Frame(self.__root, bg="#E2E9C0")
        self.__frame1.pack(side=TOP)
        self.__label1 = Label(self.__frame1, text="CHOOSE YOUR SETUP", font=("Arial", 16), bg="#E2E9C0", fg="#25416B")
        self.__label1.pack(side=LEFT, padx=10, pady=10)

        self.__frame2 = Frame(self.__root)
        self.__frame2.pack(side=TOP)
        self.__label2 = Label(self.__frame2, image=setup1, bg="#E2E9C0")
        self.__label2.pack(side=LEFT, padx=10, pady=10)
        self.__label3 = Label(self.__frame2, image=setup2, bg="#E2E9C0")
        self.__label3.pack(side=LEFT, padx=10, pady=10)
        self.__label4 = Label(self.__frame2, image=setup3, bg="#E2E9C0")
        self.__label4.pack(side=LEFT, padx=10, pady=10)
        self.__label5 = Label(self.__frame2, image=setup4, bg="#E2E9C0")
        self.__label5.pack(side=LEFT, padx=10, pady=10)
        self.__label6 = Label(self.__frame2, image=setup5, bg="#E2E9C0")
        self.__label6.pack(side=LEFT, padx=10, pady=10)

        self.__frame3 = Frame(self.__root)
        self.__frame3.pack(side=TOP)
        self.__button1 = Button(self.__frame3, text="CHOOSE", bg="#25416B", fg="#FFFFFF", command=lambda: self.setGridSizeValue(1))
        self.__button1.pack(side=LEFT, padx=60, pady=10)
        self.__button2 = Button(self.__frame3, text="CHOOSE", bg="#25416B", fg="#FFFFFF", command=lambda: self.setGridSizeValue(2))
        self.__button2.pack(side=LEFT, padx=65, pady=10)
        self.__button3 = Button(self.__frame3, text="CHOOSE", bg="#25416B", fg="#FFFFFF", command=lambda: self.setGridSizeValue(3))
        self.__button3.pack(side=LEFT, padx=50, pady=10)
        self.__button4 = Button(self.__frame3, text="CHOOSE", bg="#25416B", fg="#FFFFFF", command=lambda: self.setGridSizeValue(4))
        self.__button4.pack(side=LEFT, padx=65, pady=10)
        self.__button5 = Button(self.__frame3, text="CHOOSE", bg="#25416B", fg="#FFFFFF", command=lambda: self.setGridSizeValue(5))
        self.__button5.pack(side=LEFT, padx=70, pady=10)

        self.__root.mainloop()

    def setGridSizeValue(self, value):
        self.__gridSizeValue = value
        self.__backgroundMusic.stop()
        self.__root.destroy()

    def getGridSizeValue(self):
        return self.__gridSizeValue


class Game(GridSelection):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        self.__clickSound = pygame.mixer.Sound("Click.wav")
        self.__backgroundMusic = pygame.mixer.Sound("Shine2.mp3")
        self.__backgroundMusic.play(-1)
        self.__root = Tk()
        self.__root.title("Fox And Geese")
        self.__root.geometry("650x450")
        self.__root.resizable(width=False, height=False)
        self.__root.iconbitmap("img\logo.ico")

    # Définition des variables
        self.__gridSizeValue = super().getGridSizeValue()
        self.__board1 = [[0, 0, 1, 1, 1, 0, 0],
                        [0, 0, 1, 1, 1, 0, 0],
                        [1, 1, 1, 2, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1],
                        [3, 3, 3, 3, 3, 3, 3],
                        [0, 0, 3, 3, 3, 0, 0],
                        [0, 0, 3, 3, 3, 0, 0]]
        self.__board2 = [[0, 0, 1, 1, 1, 0, 0],
                        [0, 0, 1, 1, 1, 0, 0],
                        [1, 1, 1, 2, 1, 1, 1],
                        [3, 1, 1, 1, 1, 1, 3],
                        [3, 3, 3, 3, 3, 3, 3],
                        [0, 0, 3, 3, 3, 0, 0],
                        [0, 0, 3, 3, 3, 0, 0]]
        self.__board3 = [[0, 0, 1, 1, 1, 0, 0],
                        [0, 0, 1, 1, 1, 0, 0],
                        [3, 1, 1, 2, 1, 1, 3],
                        [3, 1, 1, 1, 1, 1, 3],
                        [3, 3, 3, 3, 3, 3, 3],
                        [0, 0, 3, 3, 3, 0, 0],
                        [0, 0, 3, 3, 3, 0, 0]]
        self.__board4 = [[0, 0, 1, 1, 1, 0, 0],
                        [0, 0, 2, 1, 2, 0, 0],
                        [1, 1, 1, 1, 1, 1, 1],
                        [3, 3, 3, 3, 3, 3, 3],
                        [3, 3, 3, 3, 3, 3, 3],
                        [0, 0, 3, 3, 3, 0, 0],
                        [0, 0, 3, 3, 3, 0, 0]]
        self.__board5 = [[0, 0, 2, 1, 2, 0, 0],
                        [0, 0, 1, 1, 1, 0, 0],
                        [3, 3, 3, 3, 3, 3, 3],
                        [3, 3, 3, 3, 3, 3, 3],
                        [3, 3, 3, 3, 3, 3, 3],
                        [0, 0, 3, 3, 3, 0, 0],
                        [0, 0, 3, 3, 3, 0, 0]]
        self.__countFox = 0
        self.__countGeese = 0
        self.__currentPlayer = 2
        self.__currentPlayerText = "FOX"
        self.__colFrom = 0
        self.__rowFrom = 0
        self.__countFoxVar = StringVar()
        self.__countGeeseVar = StringVar()
        self.__currentPlayerVar = StringVar()
        self.__possibleMooveFox = True
        self.__possibleMooveGeese = True

    # Frame pour la grille de jeu
        self.__frame1 = Frame(self.__root, bg="#E2E9C0")
        self.__frame1.grid(row=0, column=0)
        self.__canvas = Canvas(self.__frame1, width=385, height=385)
        self.__canvas.pack()
        self.__canvas.bind('<Button-1>', self.onClick)

    # Frame pour les statistiques
        self.__frame2 = Frame(self.__root)
        self.__frame2.grid(row=0, column=1)
        self.__label1 = Label(self.__frame2, text="Remaining FOX : " + str(self.__countFox), font=("Arial", 16), fg="#25416B")
        self.__label1.pack(side=TOP, padx=10, pady=10)
        self.__label2 = Label(self.__frame2, text="Remaining GEESE : " + str(self.__countGeese), font=("Arial", 16), fg="#25416B")
        self.__label2.pack(side=TOP, padx=10, pady=10)
        self.__label3 = Label(self.__frame2, text= str(self.__currentPlayerText) + " to play ! ", font=("Arial", 16), fg="#25416B")
        self.__label3.pack(side=TOP, padx=10, pady=10)

    # Frame pour les boutons
        self.__frame3 = Frame(self.__root)
        self.__frame3.grid(row=1, column=0)
        self.__button1 = Button(self.__frame3, text="RESTART", bg="#25416B", fg="#FFFFFF", command=lambda: self.win())
        self.__button1.pack(side=LEFT, padx=10, pady=10)
        self.__button2 = Button(self.__frame3, text="LEAVE", bg="#25416B", fg="#FFFFFF", command = lambda: self.__root.destroy())
        self.__button2.pack(side=RIGHT, padx=10, pady=10)

        self.choiceBoard()
        self.displayWindow()
        self.countPawn()
        self.__root.mainloop()

    def choiceBoard(self):
        if self.__gridSizeValue == 1:
            self.__board = self.__board1
        elif self.__gridSizeValue == 2:
            self.__board = self.__board2
        elif self.__gridSizeValue == 3:
            self.__board = self.__board3
        elif self.__gridSizeValue == 4:
            self.__board = self.__board4
        elif self.__gridSizeValue == 5:
            self.__board = self.__board5

    def displayWindow(self):
        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                x = j * 55 + 55 // 2
                y = i * 55 + 55 // 2
            # Affichage pions noir
                if self.__board[i][j] == 1:
                    self.__canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill="black")
                    self.displayLine(i, j, x, y)
            # Affichage pions rouge / renard
                if self.__board[i][j] == 2:
                    self.__canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill="red")
                    self.displayLine(i, j, x, y)
            # Affichage pions vert / oie
                if self.__board[i][j] == 3:
                    self.__canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill="green")
                    self.displayLine(i, j, x, y)
            # Affichage des futurs déplacements sans capture possible
                if self.__board[i][j] == 4:
                    self.__canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill="blue")
                    self.displayLine(i, j, x, y)
            # Affichage des futurs déplacements avec capture possible
                if self.__board[i][j] == 5:
                    self.__canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill="purple")
                    self.displayLine(i, j, x, y)

    def displayLine(self, i, j, x, y):
    # Vérification du point au-dessus
        if i > 0 and self.__board[i - 1][j] != 0:
            self.__canvas.create_line(x, y, x, y - 55)
    # Vérification du point en dessous
        if i < len(self.__board) - 1 and self.__board[i + 1][j] != 0:
            self.__canvas.create_line(x, y, x, y + 55)
    # Vérification du point à gauche
        if j > 0 and self.__board[i][j - 1] != 0:
            self.__canvas.create_line(x, y, x - 55, y)
    # Vérification du point à droite
        if j < len(self.__board[i]) - 1 and self.__board[i][j + 1] != 0:
            self.__canvas.create_line(x, y, x + 55, y)

    def intToPlayer(self):
        if self.__currentPlayer == 2:
            self.__currentPlayerText = "Fox"
        elif self.__currentPlayer == 3:
            self.__currentPlayerText = "Geese"
        return self.__currentPlayerText

    def countPawn(self):
        self.__countFox = 0
        self.__countGeese = 0
        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                if self.__board[i][j] == 2:
                    self.__countFox += 1
                elif self.__board[i][j] == 3:
                    self.__countGeese += 1
        self.__countFoxVar.set(str(self.__countFox))
        self.__countGeeseVar.set(str(self.__countGeese))
        self.__label1.config(text="Remaining FOX: " + self.__countFoxVar.get())
        self.__label2.config(text="Remaining GEESE: " + self.__countGeeseVar.get())
        self.__label3.config(text=self.__currentPlayerText + " to play !")
        return self.__countFox, self.__countGeese

    def definePlayer(self):
        if self.__currentPlayer == 2:
            self.__currentPlayer = 3
        elif self.__currentPlayer == 3:
            self.__currentPlayer = 2
        return self.__currentPlayer

    def onClick(self, event):
        col = event.x // 55
        row = event.y // 55
        if 0 <= row < 7 and 0 <= col < 7:
            if self.__currentPlayer == 2 and self.__board[row][col] == 2: # Déplacement du renard
                self.clearBoard()
                self.__colFrom = event.x // 55
                self.__rowFrom = event.y // 55
                if self.__board[row+1][col] == 1 and 0 <= row+1 < 7:
                    self.__board[row+1][col] = 4
                if self.__board[row-1][col] == 1 and 0 <= row-1 < 7:
                    self.__board[row-1][col] = 4
                if self.__board[row][col+1] == 1 and 0 <= col+1 < 7:
                    self.__board[row][col+1] = 4
                if self.__board[row][col-1] == 1 and 0 <= col-1 < 7:
                    self.__board[row][col-1] = 4
            # Vérification diagonales
                if self.__board[row+1][col+1] == 1 and 0 <= row+1 < 7 and 0 <= col+1 < 7:
                    self.__board[row+1][col+1] = 4
                if self.__board[row+1][col-1] == 1 and 0 <= row+1 < 7 and 0 <= col-1 < 7:
                    self.__board[row+1][col-1] = 4
                if self.__board[row-1][col-1] == 1 and 0 <= row-1 < 7 and 0 <= col-1 < 7:
                    self.__board[row - 1][col-1] = 4
                if self.__board[row-1][col+1] == 1 and 0 <= row-1 < 7 and 0 <= col+1 < 7:
                    self.__board[row-1][col + 1] = 4
            # Vérification pour une capture
                if self.__board[row+1][col] == 3 and 0 <= row + 1 < 7 and self.__board[row+2][col] == 1:
                    self.__board[row+2][col] = 5
                if self.__board[row-1][col] == 3 and 0 <= row - 1 < 7 and self.__board[row-2][col] == 1:
                    self.__board[row-2][col] = 5
                if self.__board[row][col+1] == 3 and 0 <= col + 1 < 7 and self.__board[row][col+2] == 1:
                    self.__board[row][col+2] = 5
                if self.__board[row][col-1] == 3 and 0 <= col - 1 < 7 and self.__board[row][col-2] == 1:
                    self.__board[row][col-2] = 5
                # Vérification diagonales
                if self.__board[row+1][col+1] == 3 and 0 <= row+1 < 7 and 0 <= col+1 < 7 and self.__board[row+2][col+2] == 1:
                    self.__board[row + 2][col + 2] = 5
                if self.__board[row+1][col-1] == 3 and 0 <= row+1 < 7 and 0 <= col-1 < 7 and self.__board[row+2][col-2] == 1:
                    self.__board[row + 2][col - 2] = 5
                if self.__board[row-1][col-1] == 3 and 0 <= row-1 < 7 and 0 <= col-1 < 7 and self.__board[row-2][col-2] == 1:
                    self.__board[row - 2][col - 2] = 5
                if self.__board[row-1][col+1] == 3 and 0 <= row-1 < 7 and 0 <= col+1 < 7 and self.__board[row-2][col+2] == 1:
                    self.__board[row - 2][col + 2] = 5
            if self.__currentPlayer == 2 and self.__board[row][col] == 4:
                self.__board[row][col] = 2
                self.__board[self.__rowFrom][self.__colFrom] = 1
                self.clearBoard()
                self.definePlayer()
            if self.__currentPlayer == 2 and self.__board[row][col] == 5:
                self.__board[row][col] = 2
                self.__board[self.__rowFrom][self.__colFrom] = 1
                self.clearBoard()
                self.capture(row, col)
                self.definePlayer()
            elif self.__currentPlayer == 3 and self.__board[row][col] == 3: # Déplacement de l'oie
                self.clearBoard()
                self.__colFrom = event.x // 55
                self.__rowFrom = event.y // 55
                if self.__board[row-1][col] == 1 and 0 <= row-1 < 7:
                    self.__board[row-1][col] = 4
                if self.__board[row][col+1] == 1 and 0 <= col+1 < 7:
                    self.__board[row][col+1] = 4
                if self.__board[row][col-1] == 1 and 0 <= col-1 < 7:
                    self.__board[row][col-1] = 4
            if self.__currentPlayer == 3 and self.__board[row][col] == 4:
                self.__board[row][col] = 3
                self.__board[self.__rowFrom][self.__colFrom] = 1
                self.clearBoard()
                self.definePlayer()
            if self.__board[row][col] == 1 or self.__board[row][col] == 0:
                self.clearBoard()
        self.displayWindow()
        self.intToPlayer()
        self.countPawn()
        self.checkWin()

# Permet de retirer toutes les cases bleues
    def clearBoard(self):
        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                if self.__board[i][j] == 4 or self.__board[i][j] == 5 or self.__board[i][j] == 6:
                    self.__board[i][j] = 1

    def capture(self, row, col):
        i = (self.__rowFrom + row) // 2
        j = (self.__colFrom + col) // 2
        self.__board[i][j] = 1

    def verifMooveGeese(self):
        rows = len(self.__board)
        cols = len(self.__board[0])

        for i in range(rows):
            for j in range(cols):
                upValid = 0 <= i - 1 < rows and self.__board[i - 1][j] == 1
                rightValid = 0 <= j + 1 < cols and self.__board[i][j + 1] == 1
                leftValid = 0 <= j - 1 < cols and self.__board[i][j - 1] == 1

                if not (upValid or rightValid or leftValid):
                    self.__possibleMooveGeese = False
                    return self.__possibleMooveGeese
        return self.__possibleMooveGeese

    def verifMooveFox(self):
        rows = len(self.__board)
        cols = len(self.__board[0])

        for i in range(rows):
            for j in range(cols):
                validMoves = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),
                    (i + 1, j + 1), (i + 1, j - 1), (i - 1, j - 1), (i - 1, j + 1)]

                for x, y in validMoves:
                    if 0 <= x < rows and 0 <= y < cols and self.__board[x][y] == 1:
                        self.__possibleMooveFox = False
                        return self.__possibleMooveFox

        return self.__possibleMooveFox

    def checkWin(self):
    # Condition de victoire pour les renards
        if self.__possibleMooveGeese == False:
            self.win()
        if self.__possibleMooveFox == False:
            self.win()
        if self.__board[6][2] == 2 or self.__board[6][3] == 2 or self.__board[6][4] == 2:
            self.win()
        elif self.__countGeese == 0:
            self.win()

    def win(self):
        self.definePlayer()
        self.intToPlayer()
        messagebox.showinfo("Fox And Geese", "The winner is : " + str(self.__currentPlayerText))
        playAgain = messagebox.askyesno("Fox And Geese", "Do you want to play again ?")
        if playAgain:
            self.__root.destroy()
            Game()
        else:
            self.__root.destroy()

test = Game()