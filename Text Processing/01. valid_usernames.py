usernames = input().split(", ")

for username in usernames:
    valid = False
    
    if 3 < len(username) < 16:
        for char in username:
            if char.isalpha() or char.isdigit() or char == "-" or char == "_":
                valid = True
            else:
                valid = False
                break
            
    if valid:
        print(username)