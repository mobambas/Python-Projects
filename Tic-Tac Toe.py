"""
Rules of the Tic-Tac Toe Game:

1. It has a 3x3 grid
2. It's a two-player game
3. A player chooses a symbol x or o
4. Players take turns to place their symbols in an empty cell of the grid
5. Aim of the game: A player needs to have the same symbols across rows or columns or one of the diagonals
6. A game can end in a draw if none of the players manage to have the same symbols across rows or columns or diagonals
"""

print("  |  |  ")
print("--------")
print("  |  |  ")
print("--------")
print("  |  |  ")

tic_tac_dict = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
print(tic_tac_dict)

for i in range(1, 4):
    print("  |  |  ")
    if i == 3:
        continue
    else:
        print("--------")


def display_row(tic_tac_dict, row_number):
    print(f"{tic_tac_dict[1 + 3 * (row_number - 1)]}  | {tic_tac_dict[2 + 3 * (row_number - 1)]} | {tic_tac_dict[3 + 3 * (row_number - 1)]}")


def horizontal_lines(n):
    print("-" * n)


def display_board(tic_tac_dict):
    for i in range(1, 4):
        display_row(tic_tac_dict, i)
        if i < 3:
            horizontal_lines(10)


display_board(tic_tac_dict)


def player_name():
    def get_symbol_choice(player_number):
        symbol = input(f"Player {player_number}, choose a symbol (x or o): ").lower()
        while symbol not in ['x', 'o']:
            print("Invalid choice. Please enter 'x' or 'o'.")
            symbol = input(f"Player {player_number}, choose a symbol (x or o): ").lower()
        return symbol

    player_1 = input("Enter Player 1 name: ")
    player_1_symbol = get_symbol_choice(1)

    player_2 = input("Enter Player 2 name: ")
    player_2_symbol = 'o' if player_1_symbol == 'x' else 'x'

    print(f"{player_1} will play with {player_1_symbol} and {player_2} will play with {player_2_symbol}")

    return ((player_1, player_1_symbol), (player_2, player_2_symbol))

((user_1, user_1_char), (user_2, user_2_char)) = player_name()

def row_check(tic_tac_dict, i, char):
    return all(tic_tac_dict[j] == char for j in range(1 + i * 3, 4 + i * 3))

def column_check(tic_tac_dict, i, char):
    return all(tic_tac_dict[j] == char for j in range(1 + i, 8 + i, 3))

def diagonal1_check(tic_tac_dict, char):
    return all(tic_tac_dict[j] == char for j in [1, 5, 9])

def diagonal2_check(tic_tac_dict, char):
    return all(tic_tac_dict[j] == char for j in [3, 5, 7])

def won(tictac_dict, char):
    flag = 0
    for i in range(0, 3):
        if row_check(tictac_dict, i, char) == True:
            flag = 1
        if column_check(tictac_dict, i, char) == True:
            flag = 1
        if diagonal1_check(tictac_dict, char) == True:
            flag = 1
        if diagonal2_check(tictac_dict, char) == True:
            flag = 1

    if flag == 1:
        return True
    else:
        return False


def complete(tic_tac_dict):
    flag = 0
    for i in range(1, 10):
        if len(tic_tac_dict[i]) == 0:
            flag = 1

    if flag == 1:
        return False  # implies grid isn't completely filled
    else:
        return True


# reference for the grid
reference_grid = {1: "1",
                  2: "2",
                  3: "3",
                  4: "4",
                  5: "5",
                  6: "6",
                  7: "7",
                  8: "8",
                  9: "9"}

# display_board(reference_grid)

# play game


def play_game(user_name, user_char, tic_tac_dict):
    cell = int(input(f"{user_name}, please select a cell from 1 to 9 where you want to put {user_char}: "))

    while cell not in range(1, 10) or tic_tac_dict[cell] != "":
        print("Invalid choice. Please select an empty cell from 1 to 9.")
        cell = int(input(f"{user_name}, please select a cell from 1 to 9 where you want to put {user_char}: "))

    tic_tac_dict[cell] = user_char
    display_board(tic_tac_dict)


# Initialize the player
current_player = 1

while True:
    if current_player == 1:
        play_game(user_1, user_1_char, tic_tac_dict)
        if won(tic_tac_dict, user_1_char):
            print(f"Congratulations {user_1}! You won the game!")
            break
    else:
        play_game(user_2, user_2_char, tic_tac_dict)
        if won(tic_tac_dict, user_2_char):
            print(f"Congratulations {user_2}! You won the game!")
            break

    if complete(tic_tac_dict):
        print("It's a draw!")
        break

    current_player = 3 - current_player  # Switch player (1 -> 2, 2 -> 1)
