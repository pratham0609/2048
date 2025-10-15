from tkinter import Tk, simpledialog
from gui import Game2048

if __name__ == "__main__":
    root = Tk()
    root.withdraw()  # hide the main window while asking for input

    size = simpledialog.askinteger("Board Size", "Enter board size (e.g., 4 for 4x4):", minvalue=2, maxvalue=10)

    if size:  # only start if user entered a number
        root.deiconify()
        Game2048(root, size)
        root.mainloop()
