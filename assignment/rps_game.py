import json
import os.path

# Defines of the amounts of wins, games and the ratio of the players
WINS = 0
GAMES = 1
RATIO = 2

def update_round(player1: str, player2: str, round_winner: str, game_scores: dict) -> None:
    """
    Updates the game_scores dictionary by incrementing the total games played for both players
    and recording a win for the round_winner if applicable.
    Input:
        player1 (str): The name of the first player.
        player2 (str): The name of the second player.
        round_winner (str): The name of the player who won the round, or "tie" if it's a draw.
        game_scores (dict): A dictionary where keys are player names and values are lists
                            storing [wins, games, ratio].
    Output:
        None: The game_scores dictionary is updated in place.
    """
    game_scores.setdefault(player1, [0, 0, 0])[GAMES] += 1
    game_scores.setdefault(player2, [0, 0, 0])[GAMES] += 1
    if round_winner != "tie":
        game_scores[round_winner][WINS] += 1


def find_winner(player1: str, choice1: str, player2: str, choice2: str) -> str | None:
    """
    Determines the winner of a round.
    Input:
        player1 (str): name of the first player
        choice1 (str): choice of the first player ("rock", "paper", "scissors")
        player2 (str): name of the second player
        choice2 (str): choice of the second player
    Output:
        str: winner's name or "tie" if it's a draw
    """
    if choice1 == choice2:
        return "tie"

    if choice1 == "rock":
        if choice2 == "scissors":
            return player1
        else:
            return player2

    elif choice1 == "scissors":
        if choice2 == "paper":
            return player1
        else:
            return player2

    elif choice1 == "paper":
        if choice2 == "rock":
            return player1
        else:
            return player2


def add_ratio(game_scores: dict, player: str) -> None:
    """
    Calculates and updates the win ratio for a specific player.
    Input:
        game_scores (dict): dictionary storing players' wins, games and ratio
        player (str): name of the player
    Output:
        None (updates game_scores in place)
    """
    wins, games, _ = game_scores[player]
    ratio = wins / games if games != 0 else 0
    game_scores[player][RATIO] = ratio


def find_best_ratio(game_scores: dict) -> str:
    """
    Finds the player with the highest win ratio. If there's a tie, returns "tie".
    Input:
        game_scores (dict): dictionary storing players' data
    Output:
        str: name of the player with the highest ratio, or "tie"
    """
    max_ratio = max(player_data[RATIO] for player_data in game_scores.values())

    best_players = [player for player, data in game_scores.items() if data[RATIO] == max_ratio]

    if len(best_players) > 1:
        return 'tie'
    return best_players[0]


def game(results_filename: str) -> str | None:
    """
    Processes the game results from a file and determines the overall winner.
    Input:
        results_filename (str): path to the file containing game results
    Output:
        str: name of the winner or "tie"
    """
    game_scores = {}

    print(f'starting the game with {results_filename}')
    if not os.path.exists(results_filename):  # Check if the results file exists
        print(f"results file {results_filename} does not exist")
        exit(1)
    else:
        with open(results_filename, 'r', encoding='utf8') as results_file:
            results_file.readline()     # Skip the header

            for line in results_file:
                player1, choice1, player2, choice2 = line.lower().split()
                round_winner = find_winner(player1, choice1, player2, choice2)
                update_round(player1, player2, round_winner, game_scores)

            for player in game_scores.keys():
                add_ratio(game_scores, player)

        return find_best_ratio(game_scores)


students = {'id1': '207080185', 'id2': '208077214'}

if __name__ == '__main__':
    with open('config-rps.json', 'r') as json_file:
        config = json.load(json_file)

    winner = game(config['results_filename'])
    print(f'the winner is: {winner}')
