#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import struct

def input_scores():
    s = []
    i = 1
    while True:
        n = int(input(f'#{i}? '))
        if n < 0:
            break
        s.append(n)
        i += 1
    return s

def get_average(s):
    total = sum(s)
    return total / len(s) if s else 0

def show_scores(s):
    for n in s:
        print(n, end=' ')
    print()

def save_scores(filename, scores):
    with open(filename, 'wb') as f:
        for score in scores:
            f.write(struct.pack('i', score))

def load_scores(filename):
    scores = []
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            while True:
                data = f.read(4)
                if not data:
                    break
                scores.append(struct.unpack('i', data)[0])
    return scores

filename = 'score.bin'

if os.path.exists(filename):
    scores = load_scores(filename)
    print('\n[파일 읽기]')
    print('\n[점수 출력]\n개인점수: ', end='')
    show_scores(scores)
    avg = get_average(scores)
    print(f'평균: {avg:.1f}')
else:
    print('[점수 입력]')
    scores = input_scores()
    print('\n[점수 출력]\n개인점수: ', end='')
    show_scores(scores)
    avg = get_average(scores)
    print(f'평균: {avg:.1f}')
    
    save_scores(filename, scores)


# In[ ]:




