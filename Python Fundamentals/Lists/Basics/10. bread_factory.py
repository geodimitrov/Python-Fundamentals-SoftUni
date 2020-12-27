#!/usr/bin/env python
# coding: utf-8

# In[3]:


#introduce variables
data = input().split("|")
energy = 100
coins = 100
bankrupt = False

#run a for loop to split events in the data; use conditions to process events
for el in data:
    text, value = el.split("-")
    value = int(value)
    
    if text == "rest":
        if energy + value > 100:
            energy = 100
            energy_gain = 100 - energy
        else:
            energy += value
            energy_gain = value
        print(f"You gained {energy_gain} energy.")
        print(f"Current energy: {energy}.")
        
    elif text == "order":
        
        if energy - 30 >= 0:
            energy -= 30
            coins += value
            print (f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        coins -= value
        
        if coins > 0:
            print(f"You bought {text}.")
        else:
            bankrupt = True
            print(f"Closed! Cannot afford {text}.")
            break

# if you are not bankrupt, print the following:        
if not bankrupt:
    print("Day completed!") 
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")


# In[ ]:




