students = int(input())
n_lectures = int(input())
initial_bonus = int(input())

bonus = 0
max_bonus = 0
n_attendances = 0

for n in range(students):
    attendances = int(input())
    bonus = attendances / n_lectures * (5 + initial_bonus)
    if bonus > max_bonus:
        max_bonus = bonus
        n_attendances = attendances

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {n_attendances} lectures.")