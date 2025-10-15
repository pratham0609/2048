import tkinter as tk
from tkinter import messagebox
from logic import (
    initialize_board, move_left, move_right, move_up, move_down,
    add_new_tile, check_game_over, check_win
)

class Game2048:
    def __init__(self, master, size):
        self.master = master
        self.master.title("2048 Game")
        self.size = size
        self.score = 0
        self.board = initialize_board(size)
        self.cell_colors = {
            0: "#cdc1b4", 2: "#eee4da", 4: "#ede0c8",
            8: "#f2b179", 16: "#f59563", 32: "#f67c5f",
            64: "#f65e3b", 128: "#edcf72", 256: "#edcc61",
            512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"
        }
        self.build_gui()
        self.update_board_gui()
        self.master.bind("<Key>", self.key_handler)

    def build_gui(self):
        frame = tk.Frame(self.master, bg="#bbada0", bd=5)
        frame.grid(pady=(100, 0))
        self.cell_labels = []

        for i in range(self.size):
            row = []
            for j in range(self.size):
                label = tk.Label(frame, text="", width=4, height=2,
                                 font=("Helvetica", 28, "bold"),
                                 bg="#cdc1b4", fg="#776e65")
                label.grid(row=i, column=j, padx=5, pady=5)
                row.append(label)
            self.cell_labels.append(row)

        self.score_label = tk.Label(self.master, text="Score: 0", font=("Helvetica", 20, "bold"))
        self.score_label.grid()

        restart_btn = tk.Button(self.master, text="Restart", command=self.restart_game,
                                bg="#8f7a66", fg="white", font=("Helvetica", 14, "bold"))
        restart_btn.grid(pady=20)

    def update_board_gui(self):
        for i in range(self.size):
            for j in range(self.size):
                value = self.board[i][j]
                label = self.cell_labels[i][j]
                label.config(text=str(value) if value != 0 else "",
                             bg=self.cell_colors.get(value, "#3c3a32"))
        self.score_label.config(text=f"Score: {self.score}")
        self.master.update_idletasks()

    def key_handler(self, event):
        key = event.keysym
        moved = False
        gained = 0

        if key == "Up":
            new_board, gained = move_up(self.board)
            moved = new_board != self.board
        elif key == "Down":
            new_board, gained = move_down(self.board)
            moved = new_board != self.board
        elif key == "Left":
            new_board, gained = move_left(self.board)
            moved = new_board != self.board
        elif key == "Right":
            new_board, gained = move_right(self.board)
            moved = new_board != self.board
        else:
            return

        if moved:
            self.board = add_new_tile(new_board)
            self.score += gained
            self.update_board_gui()

            if check_win(self.board):
                messagebox.showinfo("2048", "Congratulations! You reached 2048!")
            elif check_game_over(self.board):
                messagebox.showinfo("Game Over", "No more moves left!")

    def restart_game(self):
        self.board = initialize_board(self.size)
        self.score = 0
        self.update_board_gui()
        