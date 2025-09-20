from tkinter import *
from tkinter import messagebox
import random

# Setting up the Main Window
root = Tk()
root.title("Playing Rock, Paper, Scissors")
root.configure(bg='pink')
root.geometry('600x400')

# Adding labels to the Main Window
label = Label(root,
              text="Hey User! Welcome to the Rock, Paper, Scissors game.",
              bg='pink', fg='purple')
label.place(x=160, y=200)

# Function to display a messagebox and proceed if OK is clicked
def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to play Rock, Paper, Scissors?")
    if MsgBox == 'ok':
        topwin()

# Adding buttons to the main window
button = Button(root,
                 text="Play",
                 command=msg,
                 bg='brown', fg='white')
button.place(x=260, y=230)

def topwin():
    top = Toplevel()
    top.title("Rock, Paper or Scissors?")
    top.configure(bg='light blue')
    top.geometry('600x350')

    # Function to show game logic
    def play_game(player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        # Update the labels to show the current selections
        player_choice_label.config(text=f"Your choice: {player_choice}")
        computer_choice_label.config(text=f"Computer's choice: {computer_choice}")

        # Determining the winner
        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            result = "You win!"
        else:
            result = "Computer wins!"

        result_label.config(text=result)

    # Creating and placeing widgets

    player_choice_label = Label(top, text="Make your choice:", bg="blue", fg="white")
    player_choice_label.pack(pady=10)

    computer_choice_label = Label(top, text="", bg="blue", fg="white")
    computer_choice_label.pack(pady=5)

    result_label = Label(top, text="", bg="black", fg="white")
    result_label.pack(pady=10)

    # Creating buttons for each choice
    button_frame = Frame(top)
    button_frame.pack()

    rock_button = Button(button_frame, text="Rock", command=lambda: play_game("Rock"))
    rock_button.pack()

    paper_button = Button(button_frame, text="Paper", command=lambda: play_game("Paper"))
    paper_button.pack()

    scissors_button = Button(button_frame, text="Scissors", command=lambda: play_game("Scissors"))
    scissors_button.pack()

    top.mainloop()

root.mainloop()