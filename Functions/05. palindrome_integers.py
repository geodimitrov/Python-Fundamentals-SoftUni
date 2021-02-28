
#Use simple logic: check if nums in reversed order match nums in original order

def palindrome_check(numbers):
    list_nums = numbers.split(", ")
    
    for element in list_nums:
        new_num = element[::-1]
        
        if new_num == element:
            print ("True")
        else:
            print ("False")
        
nums = input()
palindrome_check(nums)

