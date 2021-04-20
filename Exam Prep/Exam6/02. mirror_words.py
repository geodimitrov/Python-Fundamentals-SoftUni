import re

text = input()

ex = r"([@#])[a-zA-Z]{3,}\1{2}[a-zA-Z]{3,}\1"

valid_pairs = [match.group() for match in re.finditer(ex, text)]
mirror_words = []

for pair in valid_pairs:
    separator = pair[0]
    word_one, word_two = pair.split(separator * 2)
    word_one = word_one[1:]
    word_two = word_two[:-1]

    if word_one[::-1] == word_two:
        mirror_words.extend([word_one, word_two])

if not valid_pairs:
    print("No word pairs found!")
else:
    print(f"{len(valid_pairs)} word pairs found!")

result = []

if not mirror_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    for i in range(0, len(mirror_words), 2):
        result.append(f"{mirror_words[i]} <=> {mirror_words[i + 1]}")
    print(", ".join(result))