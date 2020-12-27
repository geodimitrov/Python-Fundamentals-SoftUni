#!/usr/bin/env python
# coding: utf-8

# In[6]:


N = int(input())  #lost fights

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
broken_shield = 0


for i in range (1, N + 1):
    if i % 2 == 0:
        expenses += helmet_price
    if i % 3 == 0:
        expenses += sword_price
        if i % 2 == 0:
            expenses += shield_price
            broken_shield += 1
            if broken_shield % 2 == 0:
                expenses += armor_price
        
print (f"Gladiator expenses: {expenses:.2f} aureus")


# In[ ]:




