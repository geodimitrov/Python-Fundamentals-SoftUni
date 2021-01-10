#!/usr/bin/env python
# coding: utf-8

# In[2]:


text = input()


for i in range(len(text)):
    emoticon = ":"
    if text[i] == ":":
        emoticon += text[i + 1]
        print(emoticon)


# In[ ]:




