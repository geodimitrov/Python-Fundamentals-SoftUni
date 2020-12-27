#!/usr/bin/env python
# coding: utf-8

# In[7]:


import math

party_size = int(input())
days = int(input())

coins_total = 0

for day in range (1, days + 1):
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
        
    coins_total += 50 - party_size * 2
    
    if day % 3 == 0:
        coins_total -= party_size * 3
    if day % 5 == 0:
        coins_total += party_size * 20
        if day % 3 == 0:
            coins_total -= party_size * 2
    
            
print (f"{party_size} companions received {math.floor(coins_total / party_size)} coins each.")


# In[ ]:




