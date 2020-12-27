
# 1. Introduce input variable
string = input()

# 2. Use the split method to split the string into list
list_string = string.split()
new_list = []

# 3. Run a for loop to filter nums using conditions

for element in list_string:
    num = int(element)
    if num > 0:
        new_list.append(-num)
    elif num < 0:
        new_list.append(abs(num))
    else:
        new_list.append(num)
        
print(new_list)

