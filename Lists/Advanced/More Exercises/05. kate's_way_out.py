deltas = [
    (0, -1), (-1, -1), (-1, 0), (-1, +1),
    (0, +1), (+1, +1), (+1, 0), (+1, -1)
]

test_matrix = [
    ["#", "#", "#", "#", "#", "#"],
    ["#", "#", " ", " ", "k", "#"],
    ["#", "#", " ", "#", "#", "#"],
    ["#", "#", " ", "#", "#", "#"]
]

wall = "#"
kate = "k"
size = 4

def get_initial_position(matrix):
    for row in range(size):
        for col in range(len(matrix[row])):
            if matrix[row][col] == kate:
                return (row, col)

def play_maze_game(init_position, matrix):
    pass


initial_position = get_initial_position(test_matrix)
play_maze_game(initial_position, test_matrix)

