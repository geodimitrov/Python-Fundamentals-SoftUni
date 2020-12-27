#!/usr/bin/env python
# coding: utf-8

# In[16]:


gifts = input().split()

command = input()

while not command == "No Money":
    gift = command.split()[1]
    
    if "OutOfStock" in command:
        gifts = [None if el == gift else el for el in gifts]
        
    elif "Required" in command:
        index = int(command.split()[2])
        if index in range(len(gifts)):
            gifts[index] = gift
    
    elif "JustInCase" in command:
        gifts[-1] = gift
        
    command = input()
    
#remove None from list

gifts = [el for el in gifts if not el == None]

print(" ".join(gifts))


# In[ ]:




