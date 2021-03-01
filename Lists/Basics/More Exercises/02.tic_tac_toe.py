# To solve this problem, we'll use multidimensional lists
def create_game_board(lines):
    game_board = []
    for line in range(lines):
        game_board.append([int(el) for el in input().split()])
    return game_board

def check_horizontal_for_win(row):
    player = row[0]
    if row.count(player) == 3:
        return True

def check_vertical_for_win(game_board, row, col):
    if game_board[row][col] == game_board[row + 1][col] and game_board[row][col] == game_board[row + 2][col]:
        return True

def check_diagonals_for_win(game_board, row=0, col=0):
    if game_board[row][col] == game_board[row+1][col+1] and game_board[row][col] == game_board[row+2][col+2]:
        return True, game_board[row][col]
    if game_board[row][col+2] == game_board[row+1][col+1] and game_board[row][col+2] == game_board[row+2][col]:
        return True, game_board[row][col+2]
    return False, 0

def check_if_player_wins(game_board):
    winning_player = 0

    # First check the horizontal lines
    for row in game_board:
        if check_horizontal_for_win(row):
            winning_player = row[0]
            return winning_player

    # After that check the vertical lines
    for c in range(len(game_board)):
        r = 0
        if check_vertical_for_win(game_board, r, c):
            winning_player = game_board[r][c]
            return winning_player

    # Check the diagonals
    won_game, winning_player = check_diagonals_for_win(game_board)
    if won_game:
        return winning_player

    return winning_player


def print_result(winning_player):
    # check whether a player won or the game was a draw
    if winning_player == 1:
            print("First player won")
    elif winning_player == 2:
            print("Second player won")
    else:
        print("Draw!")

# the lines of the board will always be 3, create the variable
LINES = 3

# Create the game board, use a function
game_board = create_game_board(LINES)

# Create a function to check if player wins
winning_player = check_if_player_wins(game_board)

# Create a function to print the result
print_result(winning_player)

#Test Input
# 2 0 1
# 0 1 0
# 1 0 2

# 0 1 0
# 2 2 2
# 1 0 0

# 1 0 2
# 0 1 2
# 1 1 0

# 0 0 0
# 0 0 0
# 0 0 0

# 0 0 1
# 0 0 0
# 0 0 0