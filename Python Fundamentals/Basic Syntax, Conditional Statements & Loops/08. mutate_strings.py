#!/usr/bin/env python
# coding: utf-8

# In[11]:


# 1. Introduce variables (2 strings)

text_one = input()
text_two = input()

for i in range(len(text_one)):
    if not text_one[i] == text_two[i]:
        text_one = text_one.replace(text_one[i], text_two[i], 1)
        print(text_one)


# In[ ]:


#Solution 2

string_one = input()
string_two = input()
new_string = list(string_one)

for i in range(len(string_one)):
    if not string_one[i] == string_two[i]:
        new_string[i] = string_two[i]
        print("".join(new_string))


# In[ ]:




