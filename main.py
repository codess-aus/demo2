import random

def main():
    print("Welcome to Rock, Paper, Scissors!")
    player_score = 0
    computer_score = 0
    rounds = 3

    for i in range(rounds):
        player = input("Enter rock, paper, or scissors: ").lower()
        while player not in ["rock", "paper", "scissors"]:
            player = input("Invalid input. Enter rock, paper, or scissors: ").lower()
        
        computer = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose {computer}")
        
        if player == computer:
            print("It's a tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print(f"Player wins! {player.capitalize()} beats {computer}.")
            player_score += 1
        else:
            print(f"Computer wins! {computer.capitalize()} beats {player}.")
            computer_score += 1
        
        # Check if one player has already won the best of 3
        if player_score == 2 or computer_score == 2:
            break

    if player_score > computer_score:
        print("Player wins the game!")
    elif player_score < computer_score:
        print("Computer wins the game!")
    else:
        print("It's a tie!")
    
    print(f"Final Score - Player: {player_score}, Computer: {computer_score}")

if __name__ == "__main__":
    main()