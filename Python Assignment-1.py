#!/usr/bin/env python
# coding: utf-8

# ### 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[20]:


for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        print(i,end=',')
        
        


# ### 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

# In[24]:


first_name = input("Enter your first name")
last_name = input("Enter your last name")
print(first_name[::-1],last_name[::-1],sep=' ')


# ### 3. Write a Python program to find the volume of a sphere with diameter 12 cm.
# ### Formula: V=4/3 * π * r3

# In[26]:


import math
V=(4/3)*(math.pi)*((12/2)**3)
print(V)


# In[ ]:




