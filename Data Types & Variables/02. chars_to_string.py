
# Solution 1

char_1 = input()
char_2 = input()
char_3 = input()

result = char_1 + char_2 + char_3
print (result)



# Solution 2

result = ""

for _ in range(3):
    char = input()
    result += char
    
print(result)

