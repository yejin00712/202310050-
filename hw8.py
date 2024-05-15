#!/usr/bin/env python
# coding: utf-8

# In[2]:


shopping_bag = {}

def buy(shoppingbag):
    print('[구입]')

    while True:
        item = input('상품명? ')
        if item == ' ':
            break
        if item == '':
            return False
        global amount
        amount = int(input('수량은? '))
        shopping_bag[item] = amount
        print(f'장바구니에 {item} 이(가) {amount}개가 담겼습니다.')
        
def show(shoppingbag):
    print(f'\n>>> 장바구니 보기: {shopping_bag}')
    
def find(shoppingbag):
    print('\n[검색]')
    t = input('장바구니에서 확인하고자 하는 상품은? ')
    if t in shopping_bag:
        print(f'{t}은(는) {amount}개가 담겨 있습니다.')
    else:
        print(f'장바구니에 {t}은(는) 없습니다.')

while True:
    if buy(shopping_bag) == False:
        break
    show(shopping_bag)
    find(shopping_bag)


# In[ ]:




