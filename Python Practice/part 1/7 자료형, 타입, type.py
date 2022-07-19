# 7 자료형, 타입, type
a = [1, 2, 3, 4, 5]
print(a, type(a))

b = (1, 2, 3, 4, 5)
print(b, type(b))

c = {1, 2, 3, 4, 5}
print(c, type(c))

d = {'a':1, 'b':2}
print(d, type(d))

'''
[1, 2, 3, 4, 5] <class 'list'>
(1, 2, 3, 4, 5) <class 'tuple'>
{1, 2, 3, 4, 5} <class 'set'>
{'a': 1, 'b': 2} <class 'dict'>
'''

a = [1,1,2,2,3]
b = (1,1,2,2,3)
c = {1,1,2,2,3}
print(a, type(a))
print(b, type(b))
print(c, type(c))
'''
[1, 1, 2, 2, 3] <class 'list'>
(1, 1, 2, 2, 3) <class 'tuple'>
{1, 2, 3} <class 'set'>
'''