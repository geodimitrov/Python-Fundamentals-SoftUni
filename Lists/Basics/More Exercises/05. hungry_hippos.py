# create deltas to check vertically as well as horizontally
deltas = [
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, +1),
    (0, +1),
    (+1, +1),
    (+1, 0),
    (+1, -1)
]

#use a func to create board
def create_board(n_rows):
    result = []
    for row in range(n_rows):
        result.append([int(el) for el in input().split()])
    return result



n = 5  # number of rows
board = create_board(n)
print(board)

for row in range(n):
    for c in range(n):
        if board[row][c] == "1":
            check_deltas()


