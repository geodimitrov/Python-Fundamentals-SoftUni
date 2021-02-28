needed_coffee = 0
#create a list with valid "events" to check for while reading the commands
valid_events = ["cat", "dog", "coding", "movie", "CAT", "DOG", "CODING", "MOVIE"]
need_extra_sleep = False

#start reading the commands; read until we receive "END"
while True:
    command = input()
    if command == "END":
        break

    if command in valid_events:
        if command.isupper():
            needed_coffee += 2
        else:
            needed_coffee += 1

    if needed_coffee > 5:
        need_extra_sleep = True
        print("You need extra sleep")
        break

if not need_extra_sleep:
    print(needed_coffee)