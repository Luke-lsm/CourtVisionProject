import os

from player import Player

## file_utils.py is responsible for handling file operations such as reading and writing player data.
## This module is created for you, but you can modify it as needed to fit your implementation.

FILENAME = "players_data.txt"

def save_players(players_dict):
    # Saves the dictionary of player objects to a text file.
    try:
        with open(FILENAME, "w") as f:
            for p in players_dict.values():
                # Format: Name, Jersey, Position, Salary, Points, Steals, Blocks, Games
                line = f"{p.name},{p.jersey_num},{p.position},{p.salary},{p.points},{p.steals},{p.blocks},{p.games_played}\n"
                f.write(line)
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")


def load_players():
    # Loads data from the text file and returns a dictionary of Player objects
    players = {}
    if not os.path.exists(FILENAME):
        return players

    try:
        with open(FILENAME, "r") as f:
            for line in f:
                if not line.strip():
                    continue  # Skip empty lines

                parts = line.strip().split(',')

                # Extract core details for the constructor
                name = parts[0]
                jersey = int(parts[1])
                pos = parts[2]
                salary = float(parts[3])

                # Create the Player object
                p = Player(name, jersey, pos, salary)

                # Load historical performance stats
                p.points = int(parts[4])
                p.steals = int(parts[5])
                p.blocks = int(parts[6])
                p.games_played = int(parts[7])

                # Add to dictionary using Jersey as the unique Key
                players[jersey] = p

        print(f"Successfully loaded {len(players)} players.")
    except Exception as e:
        print(f"Error loading file: {e}")
        print("Check that players.txt follows the correct format.")

    return players