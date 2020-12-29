
def password_validator(password):
    is_valid = True
   
    if not 6 <= len(password) <= 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")
        
    for char in password:
        if char.isdigit() or char.isalpha():
            continue
        else:
            is_valid = False
            print ("Password must consist only of letters and digits")
            break
            
    digits = 0
    for char in password:
        if char.isdigit():
            digits += 1
    
    if digits < 2:
        is_valid = False
        print ("Password must have at least 2 digits")
        
    return is_valid
            
pass_input = input()
is_valid = password_validator(pass_input)

if is_valid:
    print ("Password is valid")

