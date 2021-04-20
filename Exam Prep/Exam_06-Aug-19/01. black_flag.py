def read_input():
    days = int(input())
    daily_plunder = int(input())
    target = float(input())

    return days, daily_plunder, target

def gather_plunder(days, daily_plunder):
    result = 0

    for day in range(1, days + 1):

        result += daily_plunder

        if day % 3 == 0:
            result += daily_plunder * 0.5

        if day % 5 == 0:
            result -= result * 0.3

    return result

def print_result(total_plunder, target):

    if total_plunder < target:
        percentage_of_target = (total_plunder / target) * 100
        print(f"Collected only {percentage_of_target:.2f}% of the plunder.")
    else:
        print(f"Ahoy! {total_plunder:.2f} plunder gained.")

days, daily_plunder, target = read_input()
total_plunder = gather_plunder(days, daily_plunder)
print_result(total_plunder, target)