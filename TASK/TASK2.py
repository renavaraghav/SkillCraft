import tkinter as tk
import random
from tkinter import messagebox

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎲 Guess the Number")
        self.root.geometry("440x380")
        self.root.configure(bg="#f4f6f7")

        self.difficulty_var = tk.StringVar(value="Medium")
        self.range_min, self.range_max = 1, 100
        self.max_attempts = 10
        self.number = None
        self.attempts = 0
        self.game_active = True

        tk.Label(root, text="🎲 Guess the Number", font=("Arial", 18, "bold"),
                 bg="#f4f6f7", fg="#2c3e50").pack(pady=(10, 8))

        frm = tk.Frame(root, bg="#f4f6f7")
        frm.pack(pady=(0, 8))
        tk.Label(frm, text="Difficulty:", font=("Arial", 11), bg="#f4f6f7").pack(side="left", padx=(0,8))
        for level in ("Easy", "Medium", "Hard"):
            tk.Radiobutton(frm, text=level, variable=self.difficulty_var, value=level,
                           command=self.set_difficulty, font=("Arial", 10),
                           bg="#f4f6f7", fg="#333").pack(side="left", padx=6)

        self.hint_label = tk.Label(root, text="", font=("Arial", 11), bg="#f4f6f7", fg="#2c3e50")
        self.hint_label.pack()

        
        self.entry = tk.Entry(root, font=("Arial", 14), width=12, justify="center")
        self.entry.pack(pady=10)
        
        self.entry.bind("<Return>", self.check_guess)

        self.button = tk.Button(root, text="Submit Guess", font=("Arial", 12, "bold"),
                                bg="#3498db", fg="white", command=self.check_guess)
        self.button.pack(pady=6)

        self.attempts_label = tk.Label(root, text="Attempts: 0 / 0",
                                       font=("Arial", 11), bg="#f4f6f7", fg="#333")
        self.attempts_label.pack()
        self.feedback = tk.Label(root, text="", font=("Arial", 12, "italic"),
                                 bg="#f4f6f7", fg="#2c3e50")
        self.feedback.pack(pady=8)

        self.reset_button = tk.Button(root, text="Restart Game", font=("Arial", 12),
                                      bg="#27ae60", fg="white", command=self.reset_game)
        self.reset_button.pack(pady=6)

        self.set_difficulty()

    def set_difficulty(self):
        level = self.difficulty_var.get()
        if level == "Easy":
            self.range_min, self.range_max, self.max_attempts = 1, 50, 10
        elif level == "Medium":
            self.range_min, self.range_max, self.max_attempts = 1, 100, 10
        else:  # Hard
            self.range_min, self.range_max, self.max_attempts = 1, 200, 12

        self.reset_game()

    def check_guess(self, event=None):
        if not self.game_active:
            return

        raw = self.entry.get().strip()
        if raw == "":
            messagebox.showwarning("Input needed", "Please enter a number.")
            return

        try:
            guess = int(raw)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")
            return

        if not (self.range_min <= guess <= self.range_max):
            messagebox.showwarning("Out of range", f"Please enter a number between {self.range_min} and {self.range_max}.")
            return

        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts} / {self.max_attempts}")

        if guess < self.number:
            self.feedback.config(text="📉 Too low! Try higher.", fg="red")
        elif guess > self.number:
            self.feedback.config(text="📈 Too high! Try lower.", fg="red")
        else:
            messagebox.showinfo("🎉 Winner!", f"Correct! You guessed it in {self.attempts} attempts.")
            self.end_game(win=True)
            return

        if self.attempts >= self.max_attempts:
            messagebox.showwarning("Game Over", f"❌ You've used {self.max_attempts} attempts!\nThe number was {self.number}.")
            self.end_game(win=False)

    def end_game(self, win: bool):
        self.game_active = False
        self.entry.config(state="disabled")
        self.button.config(state="disabled")
        if not win:
            self.feedback.config(text=f"The number was {self.number}.", fg="#2c3e50")

    def reset_game(self):
        self.number = random.randint(self.range_min, self.range_max)
        self.attempts = 0
        self.game_active = True

        # UI reset
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.button.config(state="normal")
        self.feedback.config(text=f"Guess a number between {self.range_min} and {self.range_max}.", fg="#2c3e50")
        self.attempts_label.config(text=f"Attempts: {self.attempts} / {self.max_attempts}")
        self.hint_label.config(text=f"Range: {self.range_min} — {self.range_max}    Max attempts: {self.max_attempts}")

        print(f"[DEBUG] secret number = {self.number}")

if __name__ == "__main__":
    root = tk.Tk()
    GuessingGame(root)
    root.mainloop()
