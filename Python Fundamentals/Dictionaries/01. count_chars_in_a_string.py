#!/usr/bin/env python
# coding: utf-8

# In[12]:


text = input()

occurrences = {}

for char in text:
    
    if not char == " ":
        if char in occurrences:
            occurrences[char] += 1
        else:
            occurrences[char] = 1
        
for key, value in occurrences.items():
    print(f"{key} -> {value}")


# In[ ]:




