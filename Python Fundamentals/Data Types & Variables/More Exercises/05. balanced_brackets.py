#!/usr/bin/env python
# coding: utf-8

# In[5]:


n_lines = int(input())
open_brackets = 0
close_brackets = 0

for i in range(n_lines):
    text = input()
    
    if text == "(":
        open_brackets += 1
    elif text == ")":
        close_brackets += 1
    else:
        continue
        
    if open_brackets == 0 and close_brackets == 1:
            print("UNBALANCED")
    elif open_brackets == 2 and close_brackets == 0:
            print("UNBALANCED")
    elif open_brackets == 1 and close_brackets == 1:
            print ("BALANCED")


# In[ ]:




