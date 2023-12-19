from random import randint

# Dictionary to map moves to emojis
moves_emojis = {
    "Rock": "🪨",
    "Paper": "📃",
    "Scissors": "✂️"
}

# List of valid moves
valid_moves = list(moves_emojis.keys())

# Function to check the winner
def check_winner(player_move, computer_move):
    if player_move == computer_move:
        return "Tie"
    elif (
        (player_move == "Rock" and computer_move == "Scissors") or
        (player_move == "Paper" and computer_move == "Rock") or
        (player_move == "Scissors" and computer_move == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
chances = 5
count = 0

print("Welcome to Rock, Paper, Scissors!")
while count < chances:
    player_move = input("\nRock, Paper, Scissors? (Type 'exit' to quit): ").capitalize()
    
    if player_move == "Exit":
        break
        
    if player_move not in valid_moves:
        print("Invalid input! Please enter Rock, Paper, or Scissors.")
        continue
    
    computer_move = valid_moves[randint(0, 2)]
    
    print(f"\nYou chose: {moves_emojis[player_move]}")
    print(f"Computer chose: {moves_emojis[computer_move]}")
    
    result = check_winner(player_move, computer_move)
    print(result)
    
    count += 1

print()
     