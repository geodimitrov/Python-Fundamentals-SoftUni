MORSE_CODE_SYMBOLS_TO_LETTERS = {'.-': 'A', '-...': 'B', '-.-.': 'C',
                    '-..': 'D', '.': 'E', '..-.': 'F',
                    '--.': 'G', '....': 'H', '..': 'I',
                    '.---': 'J', '-.-': 'K', '.-..': 'L',
                    '--': 'M', '-.': 'N', '---': 'O',
                    '.--.': 'P', '--.-': 'Q', '.-.': 'R',
                    '...': 'S', '-': 'T', '..-': 'U',
                    '...-': 'V', '.--': 'W', '-..-': 'X',
                    '-.--': 'Y', '--..': 'Z'
                }

def find_eng_word(code, MORSE_CODE_SYMBOLS_TO_LETTERS):
    morse_symbols = code.split()
    eng_word = ""
    for symbol in morse_symbols:
        eng_word += MORSE_CODE_SYMBOLS_TO_LETTERS[symbol]
    return eng_word

def decrypt_message(msg, MORSE_CODE_SYMBOLS_TO_LETTERS):
    result = []
    for morse_code in msg:
        eng_word = find_eng_word(morse_code, MORSE_CODE_SYMBOLS_TO_LETTERS)
        result.append(eng_word)
    return result

def print_result(decrypted_message):
    return print(" ".join(decrypted_message))


message = input().split(" | ")
decrypted_message = decrypt_message(message, MORSE_CODE_SYMBOLS_TO_LETTERS)
print_result(decrypted_message)