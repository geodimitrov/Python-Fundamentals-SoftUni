#!/usr/bin/env python
# coding: utf-8

# In[6]:


# 1. Introduce input variable

year = int(input())

# 2. Start from next year (year + 1)
year += 1

# 3. Run a while loop, check for a year with unique digits
while len(str(year)) != len(set(str(year))):
    year += 1
    
print (year)


# In[ ]:




