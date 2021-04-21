employee_one = int(input())
employee_two = int(input())
employee_three = int(input())
total_ppl = int(input())

ppl_per_hour = employee_one + employee_two + employee_three
time_needed = 0

while total_ppl > 0:
    time_needed += 1
    if time_needed % 4 == 0:
        time_needed += 1
    total_ppl -= ppl_per_hour

print(f"Time needed: {time_needed}h.")