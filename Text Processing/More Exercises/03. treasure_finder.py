#use regex to split the modified string and extract treasure type & coordinates.
import re

def read_messages():
    result = []
    while True:
        message = input()
        if message == "find":
            break
        result.append(message)
    return result

def decrypt_message(key, message):
    key_counter = 0
    result = ""
    for char in message:
        char = chr(ord(char) - key[key_counter])
        result += char

        if key_counter == 3:
            key_counter = 0
        else:
            key_counter += 1
    return result

def print_result(decrypted_message):
    global TREASURE_SEPARATOR, COORDINATES_SEPARATOR
    treasure = re.split(TREASURE_SEPARATOR, decrypted_message)[1]
    coordinates = re.split(COORDINATES_SEPARATOR, decrypted_message)[1]
    return print(f"Found {treasure} at {coordinates}")

def decrypt_messages(key, messages):
    for msg in messages:
        decrypted_message = decrypt_message(key, msg)
        print_result(decrypted_message)


TREASURE_SEPARATOR = "[&&]"
COORDINATES_SEPARATOR = "[<>]"
key = [int(el) for el in input().split()]
messages = read_messages()
decrypt_messages(key, messages)