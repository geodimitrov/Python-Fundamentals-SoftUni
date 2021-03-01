text = "abv>1>1>2>2asdasd"
new_text = ""

for i in range(len(text)):
    if not text[i] == ">":
        new_text += text[i]
    else:
        new_text += ">"
        explosion_strength = int(text[i+1])
        print(explosion_strength)