import random

def game():
    choices = ["rock", "paper", "scissors"]
    player_wins = 0
    computer_wins = 0

    print("Welcome to Rock, Paper, Scissors!")

    while True:
        player = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()

        if player == 'q':
            break
        elif player not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer = random.choice(choices)

        print(f"\nYour choice: {player}")
        print(f"Computers choice: {computer}")

        if player == computer:
            print("It's a tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You win!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

        print(f"Score: You {player_wins} - {computer_wins} Computer\n")

    print(f"\nFinal Score: You {player_wins} - {computer_wins} Computer")
    print("Thanks for playing!")

if __name__ == "__main__":
    game()