text = input()
cap_letters = []

for index in range(len(text)):
    letter = text[index]
    if letter.isupper():
        cap_letters.append(index)
    
print(cap_letters)