#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_radius(prompt):    
    r = int(input(prompt))
    return r;

def get_circle_area():
    area = 3.14*int(r)*int(r)
    return area

r = get_radius("넓이를 구하고자 하는 원의 반지름은? ")
result = get_circle_area()
print("반지름이", r, "인 원의 넓이 = 3.14 x", r, "x", r, "=", result)

r = get_radius("넓이를 구하고자 하는 원의 반지름은? ")
result = get_circle_area()
print("반지름이", r, "인 원의 넓이 = 3.14 x", r, "x", r, "=", result)


# In[ ]:




