# Rock-Paper-Scissors Minigame
import random

def get_computer_choice():
	return random.choice(['rock', 'paper', 'scissors'])

def get_player_choice():
	valid_choices = ['rock', 'paper', 'scissors']
	while True:
		choice = input("Choose rock, paper, or scissors: ").strip().lower()
		if choice in valid_choices:
			return choice
		print("Invalid option. Please choose 'rock', 'paper', or 'scissors'.")

def determine_winner(player, computer):
	if player == computer:
		return 'tie'
	elif (
		(player == 'rock' and computer == 'scissors') or
		(player == 'scissors' and computer == 'paper') or
		(player == 'paper' and computer == 'rock')
	):
		return 'win'
	else:
		return 'lose'

def play_game():
	score = 0
	rounds = 0
	while True:
		player_choice = get_player_choice()
		computer_choice = get_computer_choice()
		print(f"You chose: {player_choice}")
		print(f"Computer chose: {computer_choice}")
		result = determine_winner(player_choice, computer_choice)
		if result == 'win':
			print("You won this round!")
			score += 1
		elif result == 'lose':
			print("You lost this round.")
		else:
			print("It's a tie.")
		rounds += 1
		play_again = input("Play again? (y/n): ").strip().lower()
		if play_again != 'y':
			break
	print(f"\nGame over! You played {rounds} round(s) and won {score} time(s).")

if __name__ == "__main__":
	play_game()