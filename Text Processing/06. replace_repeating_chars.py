text = input()
new_text = text[0]

for i in range(1, len(text)):
    if not text[i - 1] == text[i]:
        new_text += text[i]

print(new_text)