#!/usr/bin/env python
# coding: utf-8

# In[3]:


def get_fixed_price(price):
    fixed_price = int(price / (1-d_rate))
    return fixed_price

d_rate = int(input("할인율은?"))/100
A = int(input("A 상품의 할인된 가격은?"))
B = int(input("B 상품의 할인된 가격은?"))

X = get_fixed_price(A)
Y = get_fixed_price(B)

print("A 상품의 정가는", X, "원")
print("B 상품의 정가는", Y, "원")


# In[ ]:




