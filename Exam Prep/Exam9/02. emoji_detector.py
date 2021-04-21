import re

EXPRESSION = r"(::|\*\*)([A-Z][a-z]{2,}\1)"

def read_input():
    return input()

def get_cool_threshold(input):
    result = 1

    for char in input:
        if char.isdigit():
            result *= int(char)

    return result

def add_emojis_to_list(input):
    result = []
    result += re.findall(EXPRESSION, input)
    formatted_result = [el[0] + el[1] for el in result]
    return formatted_result

def get_emojis(input):
    emojis = add_emojis_to_list(input)
    return emojis

def calc_emoji_coolness(emoji):
    result = 0

    for char in emoji:
        if not char == ":" and not char == "*":
            result += ord(char)

    return result

def get_cool_emojis(threshold, emojis):
    result = []

    for emoji in emojis:
        emoji_coolness = calc_emoji_coolness(emoji)
        if emoji_coolness > threshold:
            result.append(emoji)

    return result

def print_result(threshold, emojis):
    cool_emojis = get_cool_emojis(threshold, emojis)
    print(f"Cool threshold: {threshold}")
    print(f"{len(emojis)} emojis found in the text. The cool ones are:")

    if cool_emojis:
        print("\n".join(cool_emojis))

input = read_input()
cool_threshold = get_cool_threshold(input)
emojis = get_emojis(input)
print_result(cool_threshold, emojis)