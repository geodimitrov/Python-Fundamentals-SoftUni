#!/usr/bin/env python
# coding: utf-8

# In[42]:


#Solution 1

text = input()
new_text = text[0]

for i in range(1, len(text)):
    if not text[i - 1] == text[i]:
        new_text += text[i]

print(new_text)


# In[ ]:




