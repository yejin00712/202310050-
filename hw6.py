#!/usr/bin/env python
# coding: utf-8

# In[2]:


def display_multiplication_table():
    for i in range(1, 10, 1):
        for dan in range(2, 6, 1):
            print(f"{dan} x {i} = {dan*i:2d}", end="\t")
        print()

    print () 
    
    for i in range(1, 10, 1):
        for dan in range(6, 10, 1):
            print(f"{dan} x {i} = {dan*i:2d}", end="\t")
        print()

display_multiplication_table()

