#Solution 1
text = input()

new_text = ""

for char in text:
    new_char = chr(ord(char) + 3)
    new_text += new_char
    
print(new_text)


#Solution 2
text = input()

for char in text:
    new_char = chr(ord(char) + 3)
    print(new_char, end="")