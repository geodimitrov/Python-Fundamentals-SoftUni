import re
from re import split

EXPRESSION = "[&&<>]"

def read_string_input():
    END = "find"
    result = []

    while True:
        text = input()

        if text == END:
            break

        result.append(text)

    return result

def get_char_and_key_number(string, key, char_index, key_num_index):
    char = string[char_index]
    key_num = key[key_num_index]

    return char, key_num

def decrease_ascii_code_of_char(char, key_num):
    result = chr(ord(char) - key_num)
    return result


def format_message(msg):
    split_msg = re.split(EXPRESSION, msg)
    treasure_type = split_msg[1]
    coordinates = split_msg[3]

    return f"Found {treasure_type} at {coordinates}"

def decrypt_string(string, key):
    num_index = 0
    message = ""

    for i in range(len(string)):

        if num_index == len(key):
            num_index = 0

        char, key_num = get_char_and_key_number(string, key, i, num_index)
        char = decrease_ascii_code_of_char(char, key_num)
        message += char
        num_index += 1

    return message

key = list(map(int, input().split()))
strings = read_string_input()

for string in strings:
    decrypted_message = decrypt_string(string, key)
    print(format_message(decrypted_message))