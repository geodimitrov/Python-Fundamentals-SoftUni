import math

def read_input():
    result = []
    for _ in range(4):
        X = float(input())
        Y = float(input())
        result.append((X, Y))

    return result

def split_points_pairs(pairs):
    pair_one = pairs[:2]
    pair_two = pairs[2:]

    return pair_one, pair_two

def format_point(first_point, second_point, dist_first_point, dist_second_point):
    if dist_first_point > dist_second_point:
        first_point, second_point = second_point, first_point

    result = f"{tuple(math.floor(el) for el in first_point)}{tuple(math.floor(el) for el in second_point)}"
    return result

def get_line_from_points(points):
    first_point, second_point = points
    dist_first_point = math.sqrt(((0 - first_point[0]) ** 2) + ((0 - first_point[1]) ** 2))
    dist_second_point = math.sqrt(((0 - second_point[0]) ** 2) + ((0 - second_point[1]) ** 2))
    points = format_point(first_point, second_point, dist_first_point, dist_second_point)
    line = dist_first_point + dist_second_point

    return line, points

def compare_lines_from_points(pair_one, pair_two):
    line_one, formatted_pair_one = get_line_from_points(pair_one)
    line_two, formatted_pair_two = get_line_from_points(pair_two)

    if line_one > line_two:
        return formatted_pair_one

    return formatted_pair_two

def print_result(result):
    print(result)

points_pairs = read_input()
pair_one, pair_two = split_points_pairs(points_pairs)
result = compare_lines_from_points(pair_one, pair_two)
print_result(result)
