import random
from typing import NoReturn


def coin_flip_game() -> NoReturn:
  games = 0
  wins = 0
  while True:
    user_choice = input("Enter 'o' for heads, 'r' for tails, or 'X' to quit: ").lower()
    if user_choice == "x":
      break
    if user_choice not in ["o", "r"]:
      print("Invalid choice. Try again.")
      continue
    computer_choice = random.choice(["o", "r"])
    print(f"Computer chose: {'heads' if computer_choice == 'o' else 'tails'}")
    if user_choice == computer_choice:
      print("You win!")
      wins += 1
    else:
      print("You lose!")
    games += 1
  print(f"Total games: {games}, Wins: {wins}")


if __name__ == "__main__":
  coin_flip_game()
