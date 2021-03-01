numbers = [int(n) for n in input().split(", ")]
boundary = 0

while numbers:
    boundary += 10
    current_group = []
    for num in numbers:
        if num <= boundary:
            current_group.append(num)
    for num in current_group:
        numbers.remove(num)
            
    print(f"Group of {boundary}'s: {current_group}")