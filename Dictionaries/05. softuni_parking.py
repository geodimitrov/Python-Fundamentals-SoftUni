
n = int(input())

registrations = {}

for i in range(n):
    command = input()
    command_type = command.split()[0]
    user = command.split()[1]
    
    if command_type == "register": 
        plate = command.split()[2]
        
        if user in registrations:
            print(f"ERROR: already registered with plate number {plate}")
        else:
            registrations[user] = plate
            print(f"{user} registered {plate} successfully")
                
    elif command_type == "unregister":
        
        if not user in registrations:
            print(f"ERROR: user {user} not found")
        else:
            print(f"{user} unregistered successfully")
            del registrations[user]
            
for user, plate in registrations.items():
    print(f"{user} => {plate}")

