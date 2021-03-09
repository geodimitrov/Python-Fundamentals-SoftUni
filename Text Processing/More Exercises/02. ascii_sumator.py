def find_ascii_sum(char1, char2, chars):
    START = ord(char1)
    END = ord(char2)
    ascii_values = []
    for char in chars:
        if START < ord(char) < END:
            ascii_values.append(ord(char))

    return sum(ascii_values)


char_one = input()
char_two = input()
characters = input()
print(find_ascii_sum(char_one, char_two, characters))