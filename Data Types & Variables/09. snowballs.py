
N = int(input())
highest_snowball_value = 0
highest_snowball_snow = 0
highest_snowball_time = 0
highest_snowball_quality = 0

for i in range (0, N):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = int((snowball_snow / snowball_time) ** snowball_quality)
    
    if snowball_value > highest_snowball_value:
        highest_snowball_value = snowball_value
        highest_snowball_snow = snowball_snow
        highest_snowball_time = snowball_time
        highest_snowball_quality = snowball_quality

print (f"{highest_snowball_snow} : {highest_snowball_time} = {highest_snowball_value} ({highest_snowball_quality})")

