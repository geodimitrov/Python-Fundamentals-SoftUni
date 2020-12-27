
# The 1st input line will be a str so use list comprehension to turn the data into nums
list_nums = [int(el) for el in input().split(", ")]
n_beggers = int(input())
list_sums = []

# Use nested for loop to calculate the money each begger collects
for begger in range(n_beggers):
    sum_begger = 0
    for i in range(begger, len(list_nums), n_beggers):
        sum_begger += list_nums[i]
    list_sums.append(sum_begger)
    
print(list_sums)

