#!/usr/bin/env python
# coding: utf-8

# In[ ]:


shopping_bag = {}

print('[구입]')

while True:
    item = input('상품명? ')
    if item == ' ' or amount == 0:
        break
    amount = int(input('수량은? '))
    shopping_bag[item] = amount
    print(f'장바구니에 {item} 이(가) {amount}개가 담겼습니다.')

print(f'\n>>> 장바구니 보기: {shopping_bag}')

print('\n[검색]')
t = input('장바구니에서 확인하고자 하는 상품은? ')
if t in shopping_bag:
    print(f'{t}은(는) {amount}개가 담겨 있습니다.')
else:
    print('이 상품은 장바구니에 담겨 있지 않습니다')


# In[ ]:




