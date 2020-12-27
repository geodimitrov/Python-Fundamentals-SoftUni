#!/usr/bin/env python
# coding: utf-8

# In[5]:


factor = int(input())
count = int(input())
result = []

# Run a for loop in range (1, count) & simply multiply all nums in the range by the factor
for i in range(1, count + 1):
    multiple = i * factor
    result.append(multiple)

print(result)


# In[ ]:




