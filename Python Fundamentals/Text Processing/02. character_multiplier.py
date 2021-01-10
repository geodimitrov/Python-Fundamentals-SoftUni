
# Solution 1

text_1, text_2 = input().split()

sum_chars = 0

if len(text_1) > len(text_2):
    for i in range(len(text_2)):
        sum_chars += ord(text_1[i]) * ord(text_2[i])
    for i in range(len(text_2), len(text_1)):
        sum_chars += ord(text_1[i])
else:
    for i in range(len(text_1)):
        sum_chars += ord(text_1[i]) * ord(text_2[i])
    for i in range(len(text_1), len(text_2)):
        sum_chars += ord(text_2[i])

print(sum_chars)


#Solution 2 (with a function)
text_1, text_2 = input().split()


def char_multiplier(text_one, text_two):
    sum_chars = 0
    for i in range(len(text_two)):
        sum_chars += ord(text_one[i]) * ord(text_two[i])
    for i in range(len(text_two), len(text_one)):
        sum_chars += ord(text_one[i])
    return sum_chars

if len(text_1) > len(text_2):
    print(char_multiplier(text_1, text_2))
else:
    print(char_multiplier(text_2, text_1))

