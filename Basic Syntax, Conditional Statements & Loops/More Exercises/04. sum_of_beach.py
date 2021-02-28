string = input().lower()
word_counter = 0

key_words = ["Sand", "Water", "Fish", "Sun"]

for word in key_words:
    if word.lower() in string:
        word_counter += string.count(word.lower())

print(word_counter)