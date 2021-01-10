
#Solution 1
# since it's not explicitly specified in description, we will not nitroduce a num but str
number = input()

# turn the str into a list (use list comprehension)
number = [digit for digit in number]

# sort the list in reverse
sorted_number = sorted(number, reverse=True)

#turn the sorted list into a number
largest_number = int("".join(sorted_number))

print(largest_number)



# Solution 2
# you can directly turn the var value into a list

number = [digit for digit in input()]

sorted_number = sorted(number, reverse=True)

print("".join(sorted_number))
