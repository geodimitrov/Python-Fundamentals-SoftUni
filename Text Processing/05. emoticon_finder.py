text = input()

for i in range(len(text)):
    emoticon = ":"
    if text[i] == ":":
        emoticon += text[i + 1]
        print(emoticon)