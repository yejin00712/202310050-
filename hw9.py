#!/usr/bin/env python
# coding: utf-8

# In[13]:


import math

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def show(self):
        print(f'({self.__x}, {self.__y})')
        
    def set(self, x, y):
        self.__x = x
        self.__y = y

    def get(self):
        return (self.__x, self.__y)

    def getWidth(self, other_point):
        return abs(self.__x - other_point.__x)

    def getHeight(self, other_point):
        return abs(self.__y - other_point.__y)

    def getArea(self, other_point):
        return self.getWidth(other_point) * self.getHeight(other_point)

    def getPerimeter(self, other_point):
        return 2 * (self.getWidth(other_point) + self.getHeight(other_point))

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__p1 = Point(x1, y1)
        self.__p2 = Point(x2, y2)

    def show(self):
        print(f'좌측 상단 꼭지점이 {self.__p1.get()}이고 우측 하단 꼭지점이 {self.__p2.get()}인 사각형입니다.')
        
    def getArea(self):
        return self.__p1.getArea(self.__p2)

    def getPerimeter(self):
        return self.__p1.getPerimeter(self.__p2)

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'넓이는 {a}, 둘레는 {p}')


# In[ ]:




