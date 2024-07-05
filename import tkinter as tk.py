import tkinter as tk
from tkinter import messagebox
import random

class Hangman(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Hangman")
        self.geometry("400x300")

        self.words = ["PYTHON", "JAVASCRIPT", "APPLE", "COMPUTER", "ORANGE", "lemon", "DEVELOPER", "HARDDISK"]
        self.word = random.choice(self.words)
        self.guessed_letters = []
        self.remaining_attempts = 6

        self.setup_ui()

    def setup_ui(self):
        self.canvas = tk.Canvas(self, width=400, height=200, bg="white")
        self.canvas.pack()

        self.word_label = tk.Label(self, text="_ " * len(self.word), font=("Arial", 24))
        self.word_label.pack(pady=20)

        self.input_frame = tk.Frame(self)
        self.input_frame.pack()

        self.letter_entry = tk.Entry(self.input_frame, font=("Arial", 18), width=3)
        self.letter_entry.pack(side=tk.LEFT, padx=5)

        self.guess_button = tk.Button(self.input_frame, text="Guess", font=("Arial", 18), command=self.guess_letter)
        self.guess_button.pack(side=tk.LEFT, padx=5)

        self.status_label = tk.Label(self, text=f"Remaining Attempts: {self.remaining_attempts}", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.draw_gallows()

    def draw_gallows(self):
        self.canvas.create_line(10, 180, 100, 180)
        self.canvas.create_line(30, 180, 30, 20)
        self.canvas.create_line(30, 20, 70, 20)
        self.canvas.create_line(70, 20, 70, 40)

    def update_hangman(self):
        if self.remaining_attempts <= 5:
            self.canvas.create_oval(60, 40, 80, 60)
        if self.remaining_attempts <= 4:
            self.canvas.create_line(70, 60, 70, 120)
        if self.remaining_attempts <= 3:
            self.canvas.create_line(70, 80, 50, 100)
        if self.remaining_attempts <= 2:
            self.canvas.create_line(70, 80, 90, 100)
        if self.remaining_attempts <= 1:
            self.canvas.create_line(70, 120, 50, 150)
        if self.remaining_attempts <= 0:
            self.canvas.create_line(70, 120, 90, 150)

    def guess_letter(self):
        letter = self.letter_entry.get().upper()
        if len(letter) != 1 or not letter.isalpha():
            messagebox.showwarning("Invalid input", "Please enter a single letter.")
            return

        if letter in self.guessed_letters:
            messagebox.showwarning("Invalid input", "You have already guessed that letter.")
            return

        self.guessed_letters.append(letter)
        self.letter_entry.delete(0, tk.END)

        if letter in self.word:
            self.update_word_label()
            if self.check_win():
                messagebox.showinfo("Congratulations!", "You've won the game!")
                self.reset_game()
        else:
            self.remaining_attempts -= 1
            self.status_label.config(text=f"Remaining Attempts: {self.remaining_attempts}")
            self.update_hangman()
            if self.remaining_attempts == 0:
                messagebox.showinfo("Game Over", f"You've lost! The word was: {self.word}")
                self.reset_game()

    def update_word_label(self):
        displayed_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        self.word_label.config(text=displayed_word)

    def check_win(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True

    def reset_game(self):
        self.word = random.choice(self.words)
        self.guessed_letters = []
        self.remaining_attempts = 6
        self.word_label.config(text="_ " * len(self.word))
        self.status_label.config(text=f"Remaining Attempts: {self.remaining_attempts}")
        self.canvas.delete("all")
        self.draw_gallows()

if __name__ == "__main__":
    game = Hangman()
    game.mainloop()
