import math

def get_half(nums):
    return math.ceil(len(nums) / 2)

def get_time(car_race):
    time = 0
    for el in car_race:
        if not el == 0:
            time += el
        else:
            time *= 0.8
    return time

def get_race_times(nums, half):
    car_one_race = nums[:half-1]
    car_two_race = list(reversed(nums[half:]))
    return get_time(car_one_race), get_time(car_two_race)

def print_result(car_one_time, car_two_time):
    if car_one_time < car_two_time:
        return print(f"The winner is left with total time: {car_one_time:.1f}")
    return print(f"The winner is right with total time: {car_two_time:.1f}")


nums = [int(el) for el in input().split()]
half = get_half(nums)
car_one_time, car_two_time = get_race_times(nums, half)
print_result(car_one_time, car_two_time)