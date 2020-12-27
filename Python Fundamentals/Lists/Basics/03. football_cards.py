#!/usr/bin/env python
# coding: utf-8

# In[9]:


# We can directly create a list of cards by using the split method
list_cards = input().split()

players_a = 11
players_b = 11

# Use for loop to "play" the game
for element in set(list_cards):
    if "A" in element:
        players_a -= 1
    else:
        players_b -= 1
        
    if players_a < 7 or players_b < 7:
        break
        
# Use conditions to determine what to print
if players_a < 7 or players_b < 7:
    print (f"Team A - {players_a}; Team B - {players_b}")
    print ("Game was terminated")
else:
    print (f"Team A - {players_a}; Team B - {players_b}")


# In[ ]:




