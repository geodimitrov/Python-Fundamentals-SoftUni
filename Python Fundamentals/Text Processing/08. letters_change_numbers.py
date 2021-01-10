#!/usr/bin/env python
# coding: utf-8

# In[28]:


data = input().split()
total_sum = 0

def find_number(text):
    result = ""
    for char in text:
        if char.isdigit():
            result += char
    return int(result)

def find_position(letter):
    if letter.isupper():
        letter_position = ord(letter) - 64
    else:
        letter_position = ord(letter) - 96
    return letter_position


for el in data:
    first_letter = el[0]
    second_letter = el[-1]
    first_position = find_position(first_letter)
    second_position = find_position(second_letter)
    number = find_number(el)
    
    if first_letter.isupper():
        number /= first_position
    else:
        number *= first_position
    
    if second_letter.isupper():
        number -= second_position
    else:
        number += second_position
    
    total_sum += number
    number = 0
    
print(F"{total_sum:.2f}")


# In[ ]:




