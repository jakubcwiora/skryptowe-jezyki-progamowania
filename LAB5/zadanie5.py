import random
from typing import NoReturn


def rock_paper_scissors() -> NoReturn:
  choices = ["rock", "paper", "scissors"]
  games = 0
  wins = 0
  while True:
    user_choice = input("Enter 'rock', 'paper', 'scissors', or 'X' to quit: ").lower()
    if user_choice == "x":
      break
    if user_choice not in choices:
      print("Invalid choice. Try again.")
      continue
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if (
      (user_choice == "rock" and computer_choice == "scissors")
      or (user_choice == "paper" and computer_choice == "rock")
      or (user_choice == "scissors" and computer_choice == "paper")
    ):
      print("You win!")
      wins += 1
    elif user_choice == computer_choice:
      print("Draw!")
    else:
      print("You lose!")
    games += 1
  print(f"Total games: {games}, Wins: {wins}")


if __name__ == "__main__":
  rock_paper_scissors()
