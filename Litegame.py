import tkinter as tk
from tkinter import messagebox
import random

class GameHub:
    def __init__(self, root):
        self.root = root
        self.root.title("LiteGame")
        self.root.geometry("600x400")

        self.main_menu_frame = tk.Frame(root)
        self.tic_tac_toe_frame = tk.Frame(root)
        self.hangman_frame = tk.Frame(root)
        self.rps_frame = tk.Frame(root)
        self.number_guess_frame = tk.Frame(root)

        for frame in (self.main_menu_frame, self.tic_tac_toe_frame, self.hangman_frame, self.rps_frame, self.number_guess_frame):
            frame.grid(row=0, column=0, sticky='nsew')

        self.create_main_menu()
        self.create_tic_tac_toe()
        self.create_hangman()
        self.create_rps()
        self.create_number_guess()

        self.show_frame(self.main_menu_frame)

    def show_frame(self, frame):
        frame.tkraise()

    # Main Menu
    def create_main_menu(self):
        tk.Label(self.main_menu_frame, text="Welcome to Game Hub!", font=("Arial", 20)).pack(pady=20)
        tk.Button(self.main_menu_frame, text="Tic-Tac-Toe", command=lambda: self.show_frame(self.tic_tac_toe_frame)).pack(pady=10)
        tk.Button(self.main_menu_frame, text="Hangman", command=lambda: self.show_frame(self.hangman_frame)).pack(pady=10)
        tk.Button(self.main_menu_frame, text="Rock, Paper, Scissors", command=lambda: self.show_frame(self.rps_frame)).pack(pady=10)
        tk.Button(self.main_menu_frame, text="Number Guessing", command=lambda: self.show_frame(self.number_guess_frame)).pack(pady=10)
        tk.Button(self.main_menu_frame, text="Exit", command=self.root.quit).pack(pady=10)

    # Tic-Tac-Toe
    def create_tic_tac_toe(self):
        tk.Label(self.tic_tac_toe_frame, text="Tic-Tac-Toe", font=("Arial", 20)).pack(pady=10)
        self.tic_tac_toe_board = ["" for _ in range(9)]
        self.tic_tac_toe_buttons = []
        self.tic_tac_toe_turn = "X"

        board_frame = tk.Frame(self.tic_tac_toe_frame)
        board_frame.pack()

        for i in range(9):
            btn = tk.Button(board_frame, text="", font=("Arial", 16), width=5, height=2,
                            command=lambda i=i: self.tic_tac_toe_click(i))
            btn.grid(row=i // 3, column=i % 3)
            self.tic_tac_toe_buttons.append(btn)

        tk.Button(self.tic_tac_toe_frame, text="Back to Menu", command=lambda: self.show_frame(self.main_menu_frame)).pack(pady=10)

    def tic_tac_toe_click(self, index):
        if self.tic_tac_toe_board[index] == "":
            self.tic_tac_toe_board[index] = self.tic_tac_toe_turn
            self.tic_tac_toe_buttons[index].config(text=self.tic_tac_toe_turn)
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Tic-Tac-Toe", f"{winner} wins!")
                self.reset_tic_tac_toe()
            elif "" not in self.tic_tac_toe_board:
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_tic_tac_toe()
            else:
                self.tic_tac_toe_turn = "O" if self.tic_tac_toe_turn == "X" else "X"

    def check_winner(self):
        win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for a, b, c in win_combinations:
            if self.tic_tac_toe_board[a] == self.tic_tac_toe_board[b] == self.tic_tac_toe_board[c] and self.tic_tac_toe_board[a] != "":
                return self.tic_tac_toe_board[a]
        return None

    def reset_tic_tac_toe(self):
        self.tic_tac_toe_board = ["" for _ in range(9)]
        for btn in self.tic_tac_toe_buttons:
            btn.config(text="")
        self.tic_tac_toe_turn = "X"

    # Hangman
    def create_hangman(self):
        tk.Label(self.hangman_frame, text="Hangman", font=("Arial", 20)).pack(pady=10)
        self.hangman_word = random.choice([
            "python", "tkinter", "hangman", "coding", "machine", "learning", "artificial", "intelligence", "algorithm", "developer",
            "networking", "database", "security", "programming", "cloud", "software", "hardware", "computer", "artificial", "neural",
            "science", "deep", "data", "science", "testing", "debugging", "compiler", "framework", "java", "csharp", "javascript",
            "html", "css", "sql", "ruby", "swift", "objective", "android", "ios", "react", "vue", "angular", "node", "django", "flask",
            "api", "machine", "learning", "robotics", "automation", "internet", "cryptography", "blockchain", "cryptocurrency"
        ])
        self.hangman_display = ["_" for _ in self.hangman_word]
        self.hangman_attempts = 6

        self.hangman_display_label = tk.Label(self.hangman_frame, text=" ".join(self.hangman_display), font=("Arial", 16))
        self.hangman_display_label.pack(pady=10)

        self.hangman_attempts_label = tk.Label(self.hangman_frame, text=f"Guesses left: {self.hangman_attempts}", font=("Arial", 12))
        self.hangman_attempts_label.pack(pady=5)

        self.hangman_input = tk.Entry(self.hangman_frame)
        self.hangman_input.pack(pady=5)

        tk.Button(self.hangman_frame, text="Guess", command=self.hangman_guess).pack(pady=5)
        tk.Button(self.hangman_frame, text="Back to Menu", command=lambda: self.show_frame(self.main_menu_frame)).pack(pady=10)

    def hangman_guess(self):
        guess = self.hangman_input.get().strip().lower()
        self.hangman_input.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Error", "Please enter a single letter.")
            return

        if guess in self.hangman_word:
            for i, letter in enumerate(self.hangman_word):
                if letter == guess:
                    self.hangman_display[i] = guess
            self.hangman_display_label.config(text=" ".join(self.hangman_display))

            if "_" not in self.hangman_display:
                messagebox.showinfo("Hangman", "You guessed the word!")
                self.reset_hangman()
        else:
            self.hangman_attempts -= 1
            self.hangman_attempts_label.config(text=f"Guesses left: {self.hangman_attempts}")
            if self.hangman_attempts == 0:
                messagebox.showinfo("Hangman", f"Game Over! The word was: {self.hangman_word}")
                self.reset_hangman()

    def reset_hangman(self):
        self.hangman_word = random.choice([
            "python", "tkinter", "hangman", "coding", "machine", "learning", "artificial", "intelligence", "algorithm", "developer",
            "networking", "database", "security", "programming", "cloud", "software", "hardware", "computer", "artificial", "neural",
            "science", "deep", "data", "science", "testing", "debugging", "compiler", "framework", "java", "csharp", "javascript",
            "html", "css", "sql", "ruby", "swift", "objective", "android", "ios", "react", "vue", "angular", "node", "django", "flask",
            "api", "machine", "learning", "robotics", "automation", "internet", "cryptography", "blockchain", "cryptocurrency"
        ])
        self.hangman_display = ["_" for _ in self.hangman_word]
        self.hangman_attempts = 6
        self.hangman_display_label.config(text=" ".join(self.hangman_display))
        self.hangman_attempts_label.config(text=f"Guesses left: {self.hangman_attempts}")

    # Rock, Paper, Scissors
    def create_rps(self):
        tk.Label(self.rps_frame, text="Rock, Paper, Scissors", font=("Arial", 20)).pack(pady=10)

        self.rps_result_label = tk.Label(self.rps_frame, text="Choose Rock, Paper, or Scissors to play!", font=("Arial", 14))
        self.rps_result_label.pack(pady=10)

        rps_buttons_frame = tk.Frame(self.rps_frame)
        rps_buttons_frame.pack()

        for choice in ["Rock", "Paper", "Scissors"]:
            tk.Button(rps_buttons_frame, text=choice, width=10, command=lambda c=choice: self.play_rps(c)).pack(side="left", padx=5)

        tk.Button(self.rps_frame, text="Back to Menu", command=lambda: self.show_frame(self.main_menu_frame)).pack(pady=10)

    def play_rps(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = ""

        if user_choice == computer_choice:
            result = "It's a draw!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You Win!"
        else:
            result = "You lose!"

        self.rps_result_label.config(text=f"You chose {user_choice}, Computer chose {computer_choice}. {result}")

    # Number Guessing
    def create_number_guess(self):
        tk.Label(self.number_guess_frame, text="Number Guessing Game", font=("Arial", 20)).pack(pady=10)

        self.number_to_guess = random.randint(1, 100)
        self.guess_input = tk.Entry(self.number_guess_frame)
        self.guess_input.pack(pady=5)

        self.number_guess_result_label = tk.Label(self.number_guess_frame, text="Guess a number between 1 and 100!", font=("Arial", 14))
        self.number_guess_result_label.pack(pady=10)

        tk.Button(self.number_guess_frame, text="Submit Guess", command=self.submit_guess).pack(pady=5)
        tk.Button(self.number_guess_frame, text="Back to Menu", command=lambda: self.show_frame(self.main_menu_frame)).pack(pady=10)

    def submit_guess(self):
        try:
            user_guess = int(self.guess_input.get())
            if user_guess < self.number_to_guess:
                self.number_guess_result_label.config(text="Too low! Try again.")
            elif user_guess > self.number_to_guess:
                self.number_guess_result_label.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Number Guessing Game", "Congratulations! You guessed the number!")
                self.number_to_guess = random.randint(1, 100)
                self.number_guess_result_label.config(text="Guess a number between 1 and 100!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
if __name__ == "__main__":
    root = tk.Tk()
    app = GameHub(root)
    root.mainloop()
