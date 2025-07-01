import tkinter as tk
import random
from tkinter import messagebox
import threading
import time

import winsound  # For sound effects on Windows

CHOICES = ['Rock', 'Paper', 'Scissors']
WIN_RULES = {
    ('Rock', 'Scissors'): True,
    ('Paper', 'Rock'): True,
    ('Scissors', 'Paper'): True
}

def play_sound(win):
    # Simple beep for win/lose/draw
    if win == "win":
        winsound.Beep(800, 200)
    elif win == "lose":
        winsound.Beep(400, 200)
    else:
        winsound.Beep(600, 200)

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.player_score = 0
        self.computer_score = 0
        self.animating = False

        self.score_label = tk.Label(root, text="Player: 0  Computer: 0", font=("Arial", 16))
        self.score_label.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.choices_frame = tk.Frame(root)
        self.choices_frame.pack(pady=10)

        self.buttons = {}
        for choice in CHOICES:
            btn = tk.Button(self.choices_frame, text=choice, width=10, font=("Arial", 12),
                            command=lambda c=choice: self.player_choice(c))
            btn.pack(side=tk.LEFT, padx=5)
            self.buttons[choice] = btn

        self.animation_label = tk.Label(root, text="", font=("Arial", 24))
        self.animation_label.pack(pady=10)

        self.play_again_btn = tk.Button(root, text="Play Again", font=("Arial", 12),
                                        command=self.reset_game, state=tk.DISABLED)
        self.play_again_btn.pack(pady=10)

    def player_choice(self, player_pick):
        if self.animating:
            return
        computer_pick = random.choice(CHOICES)
        self.animate_choices(player_pick, computer_pick)

    def animate_choices(self, player_pick, computer_pick):
        self.animating = True
        self.animation_label.config(text="Rock...")
        self.root.update()
        self.root.after(400, lambda: self.animation_label.config(text="Paper..."))
        self.root.after(800, lambda: self.animation_label.config(text="Scissors..."))
        self.root.after(1200, lambda: self.show_result(player_pick, computer_pick))

    def show_result(self, player_pick, computer_pick):
        self.animation_label.config(text=f"You: {player_pick}  |  Computer: {computer_pick}")
        result = self.determine_winner(player_pick, computer_pick)
        if result == "win":
            self.player_score += 1
            msg = "You win this round!"
        elif result == "lose":
            self.computer_score += 1
            msg = "Computer wins this round!"
        else:
            msg = "It's a draw!"
        self.score_label.config(text=f"Player: {self.player_score}  Computer: {self.computer_score}")
        self.result_label.config(text=msg)
        threading.Thread(target=play_sound, args=(result,), daemon=True).start()
        self.check_game_over()
        self.animating = False

    def determine_winner(self, player, computer):
        if player == computer:
            return "draw"
        elif WIN_RULES.get((player, computer), False):
            return "win"
        else:
            return "lose"

    def check_game_over(self):
        if self.player_score == 3 or self.computer_score == 3:
            if self.player_score == 3:
                final_msg = "Congratulations! You won the match!"
            else:
                final_msg = "Sorry, the computer won the match."
            self.result_label.config(text=final_msg)
            for btn in self.buttons.values():
                btn.config(state=tk.DISABLED)
            self.play_again_btn.config(state=tk.NORMAL)

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.score_label.config(text="Player: 0  Computer: 0")
        self.result_label.config(text="")
        self.animation_label.config(text="")
        for btn in self.buttons.values():
            btn.config(state=tk.NORMAL)
        self.play_again_btn.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()