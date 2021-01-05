#!/usr/bin/env python
# coding: utf-8

# In[59]:


data = input()

forceusers = {}

while not data == "Lumpawaroo":
    
    if "|" in data:
        side, user = data.split(" | ")
        is_found = False
        
        for value in forceusers.values():
            if user in value:
                is_found = True
        if not is_found:
            if side not in forceusers:
                forceusers[side] = []
            forceusers[side].append(user)

        
    elif "->" in data:
        user, side = data.split(" -> ")
        if side not in forceusers:
            forceusers[side] = []
            
        for key, value in forceusers.items():
            if user in value:
                forceusers[key].remove(user)
                
        forceusers[side].append(user)
        print(f"{user} joins the {side} side!")
                   
    data = input()

forceusers = dict(sorted(forceusers.items(), key=lambda x: (-len(x[1]), x[0])))
    
for side, users in forceusers.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in sorted(users):
            print(f"! {user}")


# In[50]:


e | b
e | a
f | d
f | c
f | e
g | e
Lumpawaroo


# In[ ]:




