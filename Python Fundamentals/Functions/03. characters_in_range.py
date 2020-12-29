
def range_characters(char_one, char_two):
    for char in range(ord(char_one) + 1, ord(char_two)):
        print(chr(char), end=" ")
    
    
char_one = input()
char_two = input()
range_characters(char_one, char_two)

