import math

# read the input with a func
def read_input():
    X1 = int(input())
    Y1 = int(input())
    X2 = int(input())
    Y2 = int(input())
    return (X1, Y1), (X2, Y2)

# create func to find the closer point to the center of the coordinate sys (0, 0)
def find_closest_point_to_center(first_point, second_point):
    #calc the distance between each point and center point(0, 0)
    dist_first_point = math.sqrt(((0 - first_point[0]) ** 2) + ((0 - first_point[1]) ** 2))
    dist_second_point = math.sqrt(((0 - second_point[0]) ** 2) + ((0 - second_point[1]) ** 2))

    #compare the dists and return the shorter one
    if dist_first_point <= dist_second_point:
        return f"{first_point}"
    return f"{second_point}"

point_one, point_two = read_input()
print(find_closest_point_to_center(point_one, point_two))