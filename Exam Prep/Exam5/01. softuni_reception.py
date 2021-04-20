
def read_input(n):
    result = 0

    for _ in range(n):
        result += (int(input()))

    return result

n = 3
employees_capacity = read_input(n)
students_to_handle = int(input())
hours_needed = 0

while students_to_handle > 0:

    hours_needed += 1

    if hours_needed % 4 == 0:
        hours_needed += 1

    students_to_handle -= employees_capacity

print(f"Time needed: {hours_needed}h.")
