
#Solution 1 (use lower() method to turn all letters lowercase before you use the regex)
import re

text = input().lower()
word = input().lower()

match = re.findall(rf"\b{word}\b", text)

print(len(match))


# In[1]:


#Solution 2 (use IGNORECASE)
import re

text = input()
word = input()

match = re.findall(rf"\b{word}\b", text, re.IGNORECASE)

print(len(match))

