from tkinter import *
import subprocess
from PIL import ImageTk, Image


class HomePage:
    def __init__(self):
        self.__root = Tk()
        self.__root.title("Fox And Geese")
        self.__root.geometry("600x300")
        self.__root.resizable(width=False, height=False)
        self.__root.configure(bg="#E2E9C0")
        self.__root.iconbitmap("img\logo.ico")
        self.__modeValue = IntVar(value=0)

        self.__logo = Image.open("img\logo.png")
        self.__logo = self.__logo.resize((150, 150))
        logo = ImageTk.PhotoImage(self.__logo)

        frame1 = Frame(self.__root, bg="#E2E9C0")
        frame1.pack(side=TOP)
        label = Label(frame1, text="FOX AND GEESE", font=("Arial", 16), bg="#E2E9C0", fg="#25416B")
        label.pack(side=LEFT, padx=10, pady=10)

        frame2 = Frame(self.__root, bg="#E2E9C0")
        frame2.pack(side=TOP)
        label2 = Label(frame2, image=logo, bg="#E2E9C0")
        label2.pack(side=LEFT, padx=10, pady=10)

        frame3 = Frame(self.__root, bg="#E2E9C0")
        frame3.pack(side=TOP)
        button1 = Button(frame3, text="Play", bg="#25416B", fg="#FFFFFF", command=lambda: self.setModeValue(1))
        button1.pack(side=LEFT, padx=10, pady=10)
        button2 = Button(frame3, text="Rules", bg="#25416B", fg="#FFFFFF", command=lambda: self.setModeValue(2))
        button2.pack(side=LEFT, padx=10, pady=10)
        button3 = Button(frame3, text="Leave", bg="#25416B", fg="#FFFFFF", command=lambda: self.__root.destroy())
        button3.pack(side=LEFT, padx=10, pady=10)

        self.__root.mainloop()

    def setModeValue(self, value):
        self.__modeValue.set(value)
        self.__root.destroy()

    def getModeValue(self):
        return self.__modeValue.get()

def executionCommand(modeValue):
    if modeValue == 1:
        subprocess.run(["python", "grid.py"])
    elif modeValue == 2:
        subprocess.run(["python", "rules.py"])
    else:
        print("Fermeture du jeu")

startHomePage = HomePage()
modeValue = startHomePage.getModeValue()
executionCommand(modeValue)
