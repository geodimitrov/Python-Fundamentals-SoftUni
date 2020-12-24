#!/usr/bin/env python
# coding: utf-8

# In[11]:


n = int(input())
capacity = 255
filled_capacity = 0

for i in range (n):
    water = int(input())
    if water > capacity:
        print ("Insufficient capacity!")
    else:
        filled_capacity += water
        capacity -= water
        
print (filled_capacity)


# In[ ]:




