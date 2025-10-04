import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
    """Check if placing num at (row, col) is valid"""
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    box_row, box_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    """Backtracking solver"""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def get_board():
    """Reads current entries into a board matrix"""
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            val = entries[i][j].get()
            if val.isdigit() and 1 <= int(val) <= 9:
                row.append(int(val))
            else:
                row.append(0)
        board.append(row)
    return board

def fill_board(board, original):
    """Fills solved board into GUI. Keeps user input black, solved ones blue."""
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            if board[i][j] != 0:
                entries[i][j].insert(0, str(board[i][j]))
                if original[i][j] == 0:
                    entries[i][j].config(fg="blue")
                else:
                    entries[i][j].config(fg="black")

def solve():
    """Handler for Solve button"""
    board = get_board()
    original = [row[:] for row in board]  # copy of user input
    if not is_valid_setup(board):
        messagebox.showerror("❌ Error", "Invalid Sudoku setup! Check your inputs.")
        return
    if solve_sudoku(board):
        fill_board(board, original)
        messagebox.showinfo("✅ Solved", "Sudoku solved successfully!")
    else:
        messagebox.showerror("❌ Error", "No solution exists!")

def clear_board():
    """Clears the Sudoku grid"""
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].config(fg="black")

def is_valid_setup(board):
    """Checks if the initial board setup is valid"""
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != 0:
                board[i][j] = 0
                if not is_valid(board, i, j, num):
                    return False
                board[i][j] = num
    return True

# ---------------- GUI Layout ----------------
root = tk.Tk()
root.title("🧩 Sudoku Solver")
root.configure(bg="#f0f4f7")

entries = [[None for _ in range(9)] for _ in range(9)]

frame = tk.Frame(root, bg="#f0f4f7")
frame.pack(pady=20)

for i in range(9):
    for j in range(9):
        e = tk.Entry(frame, width=3, font=("Arial", 14), justify="center")
        e.grid(row=i, column=j, 
               padx=(2 if j % 3 == 0 else 0, 2), 
               pady=(2 if i % 3 == 0 else 0, 2))
        entries[i][j] = e

btn_frame = tk.Frame(root, bg="#f0f4f7")
btn_frame.pack(pady=10)

btn_solve = tk.Button(btn_frame, text="Solve Sudoku", font=("Arial", 12, "bold"),
                      bg="#4CAF50", fg="white", command=solve)
btn_solve.grid(row=0, column=0, padx=5)

btn_clear = tk.Button(btn_frame, text="Clear Board", font=("Arial", 12, "bold"),
                      bg="#e74c3c", fg="white", command=clear_board)
btn_clear.grid(row=0, column=1, padx=5)

root.mainloop()
