#!/usr/bin/env python
# coding: utf-8

# In[5]:


data = input()
counter = 0

resources = {}

while not data == "stop":
    counter += 1
    if not counter % 2 == 0:
        resource_name = data
    else:
        quantity = int(data)
        if resource_name in resources:
            resources[resource_name] += quantity
        else:
            resources[resource_name] = quantity
    
    data = input()

for key, value in resources.items():
    print(f"{key} -> {value}")


# In[ ]:




