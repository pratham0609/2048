from tkinter import Tk
from gui import Game2048

if __name__ == "__main__":
    root = Tk()
    size = int(input("Enter board size (e.g., 4 for 4x4): "))
    Game2048(root, size)
    root.mainloop()
