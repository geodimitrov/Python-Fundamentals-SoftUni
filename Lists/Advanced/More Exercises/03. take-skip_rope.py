def sep_digits_from_non_digits(string):
    nums = []
    non_nums = []

    for char in string:
        if char.isdigit():
            nums.append(char)
        else:
            non_nums.append(char)

    return nums, "".join(non_nums)

def split_nums(nums):
    evens = []
    odds = []

    for i in range(len(nums)):
        if i % 2 == 0:
            evens.append(int(nums[i]))
        else:
            odds.append(int(nums[i]))

    return evens, odds

def decrypt_message(text, take_nums, skip_nums):
    result = ""
    curr_index = 0

    for i in range(len(take_nums)):
        take_num = take_nums[i]
        skip_num = skip_nums[i]

        result += text[curr_index:curr_index + take_num]
        curr_index += skip_num + take_num

    return result

def print_result(result):
    print(result)

string = input()
numbers, non_numbers = sep_digits_from_non_digits(string)
take_list, skip_list = split_nums(numbers)
result = decrypt_message(non_numbers, take_list, skip_list)
print_result(result)