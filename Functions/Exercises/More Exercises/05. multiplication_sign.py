def read_input(n=3):
    return [int(input()) for _ in range(n)]

def zero_in_nums(nums):
    return 0 in nums

def count_negative_nums(nums):
    counter = 0
    for num in nums:
        if num < 0:
            counter += 1
    return counter

def check_product(nums):
    if zero_in_nums(nums):
        return "zero"

    negative_nums = count_negative_nums(nums)
    if negative_nums == 1 or negative_nums == 3:
        return "negative"
    return "positive"

nums = read_input()
print(check_product(nums))