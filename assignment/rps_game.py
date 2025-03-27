import json

def find_winner(choice1, choice2):
    if choice1 == "rock" and choice2 == "scissors":
        return 1
    elif choice1 == "scissors" and choice2 == "rock":
        return 2
    elif choice1 == "scissors" and choice2 == "paper":
        return 1
    elif choice1 == "paper" and choice2 == "scissors":
        return 2
    elif choice1 == "paper" and choice2 == "rock":
        return 1
    elif choice1 == "rock" and choice2 == "paper":
        return 2
    else:
        return 0

def game(results_filename):
    # todo: implement this function
    print(f'starting the game with {results_filename}')

    # todo: due to possible difference in file encodings between operating systems, you may need to add
    #  utf8 encoding type when opening a file, as an example: with open(<file name>, 'r', encoding='utf8') as fin
    #  python developers plan to make utf8 a default at 3.15 - https://peps.python.org/pep-0686/


    winner = ''  # todo: assign player name or "tie"
    return winner


# todo: fill in your student ids
students = {'id1': '207080185', 'id2': '208077214'}

if __name__ == '__main__':
    with open('config-rps.json', 'r') as json_file:
        config = json.load(json_file)

    with open('rps-results.txt', 'r') as results_file:
        lines = file.readlines()
        game_dict = {}
        for index, line in enumerate(lines, start=1):
            temporary_loaded_line = line.split()
            round_result = find_winner(temporary_loaded_line[1], temporary_loaded_line[3])

            game_dict.setdefault(temporary_loaded_line[0], [0, 0])
            game_dict.setdefault(temporary_loaded_line[2], [0, 0])

            if round_result == 1:
                game_dict[temporary_loaded_line[0]][0] += 1
                game_dict[temporary_loaded_line[0]][1] += 1
                game_dict[temporary_loaded_line[2]][1] += 1

            elif round_result == 2:
                game_dict[temporary_loaded_line[2]][0] += 1
                game_dict[temporary_loaded_line[2]][1] += 1
                game_dict[temporary_loaded_line[0]][1] += 1

            else:
                game_dict[temporary_loaded_line[0]][1] += 1
                game_dict[temporary_loaded_line[2]][1] += 1

            print(f"{index}: {line.strip()}")

            win_rate_array = []
            for name, nums in game_dict.items():
                wins, games = nums
                ratio = wins / games if games != 0 else 0
                win_rate_array.append(ratio)



    winner = game(config['results_filename'])
    print(f'the winner is: {winner}')
