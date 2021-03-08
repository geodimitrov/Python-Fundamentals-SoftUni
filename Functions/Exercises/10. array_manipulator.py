def invalid_index(index, array):
    if index < 0 or index not in range(len(array)):
        return True

def find_nums(array, nums_type, odd):
    if nums_type == odd:
        return [num for num in array if not num % 2 == 0]
    return [num for num in array if num % 2 == 0]

def find_max_min_num(command_type, nums):
    if command_type == "max":
        return max(nums)
    return min(nums)

def execute_max_min_command(array, command_type, nums_type, odd):
    # find the odds/evens
    nums = find_nums(array, nums_type, odd)
    # check if there are any
    if not nums:
        return print("No matches")
    # find the max/min num
    num = find_max_min_num(command_type, nums)
    # return the index of the num
    return print(array.index(num))

def invalid_count(array, count):
    return count > len(array)

def count_bigger_than_nums(nums, count):
    return count > len(nums)

def count_less_than_nums(nums, count, command_type):
    if command_type == "first":
        return [nums[i] for i in range(count)]
    reversed_nums = reversed(nums)
    return [reversed_nums[i] for i in range(count)]


def run_command(command_type, nums, count):
    result = []
    if not nums:
        return print(result)

    if count_bigger_than_nums(nums, count):
        result = nums
    else:
        result = count_less_than_nums(nums, count, command_type)

    return print(result)

def execute_count_command(array, command_type, count, nums_type, odd):
    if invalid_count(array, count):
        return print("Invalid count")
    nums = find_nums(array, nums_type, odd)
    run_command(command_type, nums, count)


#read input and use comprehension to turn nums into ints
array = [int(el) for el in input().split()]
#use constants for end command, odd & even, it's more Pythonic
END = "end"
ODD = "odd"

#start reading the commands:
while True:
    command = input()
    # break the loop if command == end
    if command == END:
        break

    if "exchange" in command:
        # split command, take 2nd element and turn into int
        split_index = int(command.split()[1])
        # use func to check if index is valid
        if invalid_index(split_index, array):
            print("Invalid index")
        else:
            array = array[split_index + 1:] + array[:split_index + 1]

    elif "max" in command or "min" in command:
        command_type, nums_type = command.split()
        execute_max_min_command(array, command_type, nums_type, ODD)

    elif "first" in command or "last" in command:
        command_type, count, nums_type = command.split()
        count = int(count)
        execute_count_command(array, command_type, count, nums_type, ODD)

print(array)