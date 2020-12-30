#!/usr/bin/env python
# coding: utf-8

# In[17]:


message = input().split()
new_message = []

for el in message:
    char_code = ""
    word = el
    
    #find the char code of the first letter
    for char in el:
        if char.isdigit():
            char_code += char
    #replace the char code with the letter to form the word
    word = word.replace(char_code, chr(int(char_code)))
    #replace the places of the 2nd & last letters of the word, to do that, turn the word into list
    word = list(word)
    word[1], word[-1] = word[-1], word[1]
    new_message.append("".join(word))

print(" ".join(new_message))


# In[7]:


char = chr("72")
char


# In[ ]:




