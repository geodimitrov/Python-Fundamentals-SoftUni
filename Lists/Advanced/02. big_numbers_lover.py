
# use list comprehension to create list from input data; the elements should be str
nums = [n for n in input().split()]

# sort the list
nums = sorted(nums, reverse=True)

# use join method to join the elements of the list into a single str
print("".join(nums))

