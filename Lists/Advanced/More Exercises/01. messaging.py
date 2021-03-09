def find_sum_digits(nums):
    result = []
    for el in nums:
        product = 0
        for digit in el:
            product += int(digit)
        result.append(product)
    return result

def index_in_range(index, string):
    return index < len(string)

def get_elements(el_indices, string):
    result = []
    for index in el_indices:
        if index_in_range(index, string):
            element = string[index]
        else:
            new_index = index % len(string)
            element = string[new_index]

        result.append(element)
        string.remove(element)
    return result

nums = input().split()
string = [char for char in input()]
el_indices = find_sum_digits(nums) #the sum of the digits are the indices of the elements from the string
elements = get_elements(el_indices, string)
print("".join(elements))