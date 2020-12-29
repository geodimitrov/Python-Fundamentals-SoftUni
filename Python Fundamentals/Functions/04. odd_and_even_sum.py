#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Solution 1 - the input is a str

def odd_even_sum(number):
    even_sum = 0
    odd_sum = 0
    
    for element in number:
        if int(element) % 2 == 0:
            even_sum += int(element)
        elif not int(element) % 2 == 0:
            odd_sum += int(element)
    print (f"Odd sum = {odd_sum}, Even sum = {even_sum}")

num = input()
odd_even_sum(num)


# In[ ]:


#Solution 2 - the input is an int

def odd_even_sum(number):
    even_sum = 0
    odd_sum = 0
    
    for element in str(number):
        if int(element) % 2 == 0:
            even_sum += int(element)
        else:                        #use else instea of elif
            odd_sum += int(element)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"  # return result instead of print

num = int(input())
print(odd_even_sum(num))

