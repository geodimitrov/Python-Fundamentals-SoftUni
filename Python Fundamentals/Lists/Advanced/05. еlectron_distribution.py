#!/usr/bin/env python
# coding: utf-8

# In[2]:


n_electrons = int(input())

distr_electrons = []
cell_position = 1

while n_electrons > 0:
    
    electrons_in_cell = 2 * cell_position ** 2
    
    if n_electrons >= electrons_in_cell:
        distr_electrons.append(electrons_in_cell)
    else:
        distr_electrons.append(n_electrons)
        
    n_electrons -= electrons_in_cell
    cell_position += 1

print(distr_electrons)


# In[ ]:




