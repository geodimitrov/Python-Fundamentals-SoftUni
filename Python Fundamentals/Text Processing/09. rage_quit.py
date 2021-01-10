#!/usr/bin/env python
# coding: utf-8

# In[26]:


data = input().upper()

text = ""
final_result = ""

for i in range(len(data)):
    number = ""
    char = data[i]
    
    if not char.isdigit():
        text += char
    
    else:
        if i + 1 < len(data) and data[i+1].isdigit():
            number = char + data[i+1]
        else:
            number = char
        final_result += text * int(number)
        text = ""

print(f"Unique symbols used: {len(set(final_result))}")
print(f"{final_result}")


# In[ ]:




