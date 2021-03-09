
def get_digits_and_non_digits(message):
    digits = []
    non_digits = []
    for char in message:
        if char.isdigit():
            digits.append(char)
        else:
            non_digits.append(char)
    return digits, non_digits

def get_take_and_skip_lists(digits):
    takes = []
    skips = []
    for i in range(len(digits)):
        if i % 2 == 0:
            takes.append(digits[i])
        else:
            skips.append(digits[i])
    return takes, skips


message = "O{1ne1T2021wf312o13Th111xreve!!@!"
digits, non_digits = get_digits_and_non_digits(message)
take_list, skip_list = get_take_and_skip_lists(digits)
print(non_digits)

for i in range(len(non_digits))
