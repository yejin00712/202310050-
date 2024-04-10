#!/usr/bin/env python
# coding: utf-8

# In[9]:


def rep_char(c, n):
    print(c*n)
    
def draw_line_string(msg1, msg2):
    nstr = len(msg1) if (len(msg1)>len(msg2)) else len(msg2)
    rep_char('-', nstr * 2)
    print(f'  {msg1}  ')
    print(f'  {msg2}  ')
    rep_char('-', nstr * 2)

n = input("Input his/her name: ")
draw_line_string(f'Hello : {n}', 'welcome to seoul.')


# In[ ]:




