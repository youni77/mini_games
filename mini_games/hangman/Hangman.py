from random import choice
import tkinter as tk


class HangMan:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hangman")
        self.window.geometry("500x400")

        self.words = [
            "apple",
            "banana",
            "orange",
            "football",
            "mother",
            "father",
            "beans",
            "peas",
            "water",
            "peach",
            "landlord",
            "glass",
            "clever",
            "loyal",
            "stupid",
            "silly",
            "children",
            "cup",
            "fork",
            "vegetarian",
            "knife",
        ]

        self.word = list(choice(self.words))
        self.turn = 1
        # self.attempt = {1: 0, 2: 0}
        self.chance = {1: 7, 2: 7}
        self.word_list = ["-" for _ in range(len(self.word))]

        self.word_label = tk.Label(
            self.window, text=" ".join(self.word_list), font=("Arial", 30)
        )
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(self.window, font=("Arial", 20), width=5)
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(
            self.window, text="Guess", font=("Arial", 16), command=self.guess
        )
        self.guess_button.pack(pady=10)

        self.message_label = tk.Label(
            self.window, text="Game Started", font=("Arial", 16)
        )
        self.message_label.pack(pady=20)

        self.status_label = tk.Label(
            self.window,
            text=f"Player {self.turn} | Chances: {self.chance[self.turn]}",
            font=("Arial", 14),
        )
        self.status_label.pack(pady=10)

    def guess(self):

        if self.chance[self.turn] == 0:
            self.message_label.config(text=f"Player {self.turn} has no chances left")
            self.switch_turn()
            return

        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)
        if guess.strip() == "":
            self.message_label.config(text="Please enter a valid letter")
            return
        if len(guess) != 1:
            self.message_label.config(text="enter just one letter!!")
            return
        if guess in self.word_list:
            self.message_label.config(text="This letter used. Guess another letter")
            return
       
        if guess in self.word:
            self.message_label.config(text=f"Player {self.turn} guessed right!")

            for i, l in enumerate(self.word):
                if l == guess:
                    self.word_list[i] = guess

            self.word_label.config(text=" ".join(self.word_list))

            if self.word_list == self.word:
                self.message_label.config(
                    text=f"Player {self.turn} wins! Word: {''.join(self.word)}"
                )
                self.guess_button.config(state="disabled")
                return

        else:
            self.message_label.config(text=f"Player {self.turn} guessed wrong")
            # self.attempt[self.turn] += 1
            self.chance[self.turn] -= 1

        self.switch_turn()

        self.status_label.config(
            text=f"Player {self.turn} | Chances: {self.chance[self.turn]}"
        )

        if self.chance[1] == 0 and self.chance[2] == 0:
            self.message_label.config(
                text=f"Both players lost! Word was {''.join(self.word)}"
            )
            self.guess_button.config(state="disabled")

    def switch_turn(self):
        self.turn = 2 if self.turn == 1 else 1


game = HangMan()
game.window.mainloop()
