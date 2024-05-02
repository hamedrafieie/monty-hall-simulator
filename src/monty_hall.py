import random
from typing import List, Tuple

def monty_hall_game(change: bool) -> bool:
    """
    Simulates a single Monty Hall game.

    Args:
        change (bool): Whether the player will switch the choice (True) or keep the initial choice (False).

    Returns:
        bool: The final choice (True for winning, False for losing).
    """
    doors: List[bool] = random.sample([False, True, False], 3)
    initial_choice: bool = random.choice(doors)
    doors.remove(initial_choice)

    if change:
        doors.remove(initial_choice)
        final_choice: bool = doors[0]
    else:
        final_choice = initial_choice

    return final_choice

def game_simulation(number_of_games: int) -> Tuple[float, float]:
    """
    Simulates multiple Monty Hall games and calculates win rates for both strategies.

    Args:
        number_of_games (int): Number of games to simulate.

    Returns:
        Tuple[float, float]: Win rate for keeping the initial choice and win rate for switching.
    """
    keep_wins: int = sum([monty_hall_game(False) for _ in range(number_of_games)])
    switch_wins: int = sum([monty_hall_game(True) for _ in range(number_of_games)])

    return keep_wins / number_of_games, switch_wins / number_of_games

# Example usage:
if __name__ == "__main__":
    num_games_to_simulate = 100000
    keep_win_rate, switch_win_rate = game_simulation(num_games_to_simulate)
    print(f"Win rate (keep): {keep_win_rate:.4f}")
    print(f"Win rate (switch): {switch_win_rate:.4f}")
