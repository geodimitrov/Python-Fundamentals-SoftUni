#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Solution 1
# 1. Introduce variables

n = int(input())  #number of people
p = int(input())  #capacity of the elevator

# 2. Use conditions to calculate result

if n % p == 0:     #if there is no remainder when we / the n of ppl to the capacity
    print(int(n / p))  # the required courses will be equal to the n of ppl / capacity
else:              # if the first condition is not true
     print ((n // p) + 1) #use floor division and add 1 more
    


# In[ ]:


# Solution 2 - use the ceil function from the math module

import math

n = int(input())  #number of people
p = int(input())  #capacity of the elevator

if n % p == 0:
    print (int(n / p))
else:
    print(math.ceil(n / p))

