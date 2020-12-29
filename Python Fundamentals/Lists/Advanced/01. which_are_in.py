
#Solution 1 - run a nested for loop

list_one = input().split(", ")
list_two = input().split(", ")
new_list = []

for el in list_one:
    for element in list_two:
        if el in element:
            new_list.append(el)
            break

print(new_list)



#Solution 2 - leave 2nd variable as str, use list comprehension
words = input().split(", ")
strings = input()

new_list = [word for word in words if word in strings]

print(new_list)

