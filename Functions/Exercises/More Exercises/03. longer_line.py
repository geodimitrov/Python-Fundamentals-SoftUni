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

# def find_closest_point_to_center(first_point, second_point):
#     dist_first_point = math.sqrt(((0 - first_point[0]) ** 2) + ((0 - first_point[1]) ** 2))
#     dist_second_point = math.sqrt(((0 - second_point[0]) ** 2) + ((0 - second_point[1]) ** 2))
#
#     if dist_first_point <= dist_second_point:
#         return first_point
#
#     return second_point


points_pairs = read_input()
pair_one, pair_two = split_points_pairs(points_pairs)


