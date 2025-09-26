# Implement the classic game against the computer. This project involves random choices, conditional logic, and simple game mechanics.with tkinter
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar, IntVar, Label, Button, Radiobutton, DISABLED, NORMAL

root = tk.Tk()
choices = ["Rock", "Paper", "Scissors"]
user_choice_var = StringVar(value="Rock")
user_score = IntVar(value=0)
computer_score = IntVar(value=0)
rounds_played = IntVar(value=0)
result_var = StringVar(value="Make your choice!")
score_var = StringVar()

def update_score_label():
    score_var.set(f"Score - You: {user_score.get()}, Computer: {computer_score.get()}")

def play_round():
    user_choice = user_choice_var.get()
    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You win this round!"
        user_score.set(user_score.get() + 1)
    else:
        result = "Computer wins this round!"
        computer_score.set(computer_score.get() + 1)
    rounds_played.set(rounds_played.get() + 1)
    result_var.set(f"You chose {user_choice}, Computer chose {computer_choice}. {result}")
    update_score_label()
    if rounds_played.get() >= 5:
        end_game()

def end_game():
    if user_score.get() > computer_score.get():
        final_result = "Congratulations! You won the game!"
    elif user_score.get() < computer_score.get():
        final_result = "Computer wins the game! Better luck next time."
    else:
        final_result = "The game is a tie!"
    messagebox.showinfo("Game Over", f"Final Score - You: {user_score.get()}, Computer: {computer_score.get()}\n{final_result}")
    play_button.config(state=DISABLED)
    for rb in choice_radiobuttons:
        rb.config(state=DISABLED)

def reset_game():
    user_score.set(0)
    computer_score.set(0)
    rounds_played.set(0)
    result_var.set("Make your choice!")
    play_button.config(state=NORMAL)
    for rb in choice_radiobuttons:
        rb.config(state=NORMAL)
    update_score_label()

root.title("Rock Paper Scissors Game")
root.geometry("400x300")
root.resizable(False, False)

Label(root, text="Choose your move:").pack(pady=10)
choice_radiobuttons = []
for choice in choices:
    rb = Radiobutton(root, text=choice, variable=user_choice_var, value=choice)
    rb.pack(anchor='w')
    choice_radiobuttons.append(rb)

play_button = Button(root, text="Play Round", command=play_round)
play_button.pack(pady=10)

result_label = Label(root, textvariable=result_var, wraplength=350)
result_label.pack(pady=10)

score_label = Label(root, textvariable=score_var)
score_label.pack(pady=10)
update_score_label()

reset_button = Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=10)

root.mainloop()
