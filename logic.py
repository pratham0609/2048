import random
import copy

def initialize_board(size=4):
    board = [[0] * size for _ in range(size)]
    board = add_new_tile(board)
    board = add_new_tile(board)
    return board

def add_new_tile(board):
    empty_cells = [(i, j) for i in range(len(board)) for j in range(len(board)) if board[i][j] == 0]
    if not empty_cells:
        return board
    i, j = random.choice(empty_cells)
    board[i][j] = random.choice([2, 4])
    return board

def compress(row):
    """Slide all non-zero tiles to the left."""
    new_row = [num for num in row if num != 0]
    new_row += [0] * (len(row) - len(new_row))
    return new_row

def merge(row):
    """Merge tiles in a single row and return score gained."""
    score = 0
    for i in range(len(row)-1):
        if row[i] != 0 and row[i] == row[i+1]:
            row[i] *= 2
            score += row[i]
            row[i+1] = 0
    return row, score

def move_left(board):
    new_board = []
    score = 0
    for row in board:
        compressed = compress(row)
        merged, gained = merge(compressed)
        final = compress(merged)
        new_board.append(final)
        score += gained
    return new_board, score

def reverse(board):
    return [row[::-1] for row in board]

def transpose(board):
    return [list(row) for row in zip(*board)]

def move_right(board):
    reversed_board = reverse(board)
    moved, score = move_left(reversed_board)
    return reverse(moved), score

def move_up(board):
    transposed = transpose(board)
    moved, score = move_left(transposed)
    return transpose(moved), score

def move_down(board):
    transposed = transpose(board)
    moved, score = move_right(transposed)
    return transpose(moved), score

def check_game_over(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return False
            if i < len(board)-1 and board[i][j] == board[i+1][j]:
                return False
            if j < len(board)-1 and board[i][j] == board[i][j+1]:
                return False
    return True

def check_win(board):
    return any(2048 in row for row in board)
