#!/usr/bin/env python
# coding: utf-8

# In[7]:


# 1. Introduce variables

divisor = int(input())
bound = int(input())
N = bound

# 2. Run a while loop that checks which is the largets int number (N) divisible by the divisor. Start from bound

while bound % divisor != 0:
    bound -= 1
    N = bound

print (N)


# In[ ]:




