#!/usr/bin/env python
# coding: utf-8

# In[20]:


def loading_bar(percentage):
    bars = 10 * "."
    
    if percentage < 100:
        for i in range(percentage // 10):
            bars = bars.replace(".", "%", 1 )
        print (f'{percentage}% [{bars}]')
        print ("Still loading...")
            
    else:
        print ("100% Complete!")
        print ("[%%%%%%%%%%]")

percentage = int(input())
loading_bar(percentage)


# In[ ]:




