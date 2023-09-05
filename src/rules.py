from tkinter import *
import subprocess
from PIL import ImageTk, Image

class Rules:
    def __init__(self):
        self.__root = Tk()
        self.__root.title("Fox And Geese")
        self.__root.geometry("950x550")
        self.__root.resizable(width=False, height=False)
        self.__root.iconbitmap("img\logo.ico")
        self.__gridSizeValue = IntVar(value=1)

    # Chargement de l'image
        self.__setup1 = Image.open("img\setup1.png")
    # Redimensionnement de l'image
        self.__setup1 = self.__setup1.resize((150, 150))
    # Conversion en image Tkinter
        setup1 = ImageTk.PhotoImage(self.__setup1)

        self.__frame1 = Frame(self.__root, bg="#E2E9C0")
        self.__frame1.pack(side=TOP)
        self.__label1 = Label(self.__frame1, text="RULES", font=("Arial", 16), bg="#E2E9C0", fg="#25416B")
        self.__label1.pack(side=LEFT, padx=10, pady=10)

        self.__frame1Bis = Frame(self.__root)
        self.__frame1Bis.pack(side=TOP)
        self.__label2 = Label(self.__frame1Bis, text='➜ Fox and Geese se joue sur un plateau de jeu de 33 cases (Voir ci-dessous). Le jeu est jouable uniquement à 2 joueurs.')
        self.__label2.pack(side=TOP, padx=10, pady=10)

        self.__frame2 = Frame(self.__root)
        self.__frame2.pack(side=TOP)
        self.__label1 = Label(self.__frame2, image=setup1, bg="#E2E9C0")
        self.__label1.pack(side=LEFT, padx=10, pady=10)
        self.__label2 = Label(self.__frame2, text="• Les oies sont représentées par les pions vert.")
        self.__label2.pack(side=TOP, padx=10, pady=10)
        self.__label3 = Label(self.__frame2, text="• Les renards sont représentés par les pions rouge.")
        self.__label3.pack(side=TOP, padx=10, pady=10)
        self.__label4 = Label(self.__frame2, text="• Les cases noires représentent des cases vides.")
        self.__label4.pack(side=TOP, padx=10, pady=10)

        self.__frame3 = Frame(self.__root)
        self.__frame3.pack(side=TOP)
        self.__label4 = Label(self.__frame3, text="➜ Un renard peut se déplacer vers une case vide adjacente dans n'importe quelle direction.")
        self.__label4.pack(side=TOP, padx=10, pady=10)
        self.__label5 = Label(self.__frame3, text="➜ Une oie peut se déplacer vers une case adjacente reliée par un trait uniquement sur une même ligne ou vers l'avant ('haut' du plateau).")
        self.__label5.pack(side=TOP, padx=10, pady=10)
        self.__label6 = Label(self.__frame3, text="➜ Un renard peut capturer une oie en passant par-dessus s'il y a une case vide juste après. \nIl faut que les trois cases en question, celle du renard, celle de l'oie et la case vide soient alignée et adjacentes. \nUn renard peut enchainer plusieurs captures selon la règle précédente.")
        self.__label6.pack(side=TOP, padx=10, pady=10)
        self.__label7 = Label(self.__frame3, text="➜ Une capture n'est pas prioritaire sur un déplacement, c'est au joueur de choisir le mouvement qu'il souhaite accomplir.")
        self.__label7.pack(side=TOP, padx=10, pady=10)
        self.__label8 = Label(self.__frame3, text="➜ Une oie ne peut pas captuer un renard.")
        self.__label8.pack(side=TOP, padx=10, pady=10)

        self.__frame4 = Frame(self.__root)
        self.__frame4.pack(side=TOP)
        self.__button1 = Button(self.__frame4, text="Back", bg="#25416B", fg="#FFFFFF",command=lambda: [self.__root.destroy(), subprocess.run(["python", "main.py"])])
        self.__button1.pack(side=LEFT, padx=60, pady=10)

        self.__root.mainloop()

Rules()