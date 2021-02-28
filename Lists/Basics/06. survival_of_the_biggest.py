
numbers = input().split()
n_remove = int(input())

# use list comprehension to turn str to nums
numbers_int = [int(num) for num in numbers]

# use for loop to go through the list; use min func to remove the min number
for i in range (n_remove):
    numbers_int.remove(min(numbers_int))
    
print(numbers_int)

