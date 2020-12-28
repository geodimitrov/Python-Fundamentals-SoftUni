#!/usr/bin/env python
# coding: utf-8

# In[3]:


#receive data as single str, use "split" to split the elements, use list comprehension to turn them into nums

numbers = [int(el) for el in input().split(", ")]

# run a for loop to locate the 0's and move them to back of list

for num in numbers:
    
    if num == 0:
        numbers.remove(num)
        numbers.append(num)
        
# print result
print(numbers)


# In[ ]:




