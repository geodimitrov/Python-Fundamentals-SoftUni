def split_negative_from_positive(nums):
    negative_nums = []
    positive_nums = []
    for num in nums:
        if num < 0:
            negative_nums.append(num)
        elif num > 0:
            positive_nums.append(num)
    return negative_nums, positive_nums

def print_result(sum_negativ, sum_positiv):
    print(sum_negativ)
    print(sum_positiv)
    if abs(sum_negativ) > sum_positiv:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")

nums = [int(el) for el in input().split()]
negative_nums, positive_nums = split_negative_from_positive(nums)

sum_positives = sum(positive_nums)
sum_negatives = sum(negative_nums)
print_result(sum_negatives, sum_positives)