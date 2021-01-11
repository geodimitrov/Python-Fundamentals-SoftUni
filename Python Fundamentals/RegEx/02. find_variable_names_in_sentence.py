#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

data = input()

ex = r"\b_[A-Za-z\d]+\b"

matches = [match.group() for match in re.finditer(ex, data)]
matches = [el.replace("_", "")for el in matches]

print(*matches, sep=",")


# In[ ]:


import re

data = input()

ex = r""

