# 16 리스트 컴프리헨션, list comprehension (1)
#pandas, numpy 등 데이터 분석에서 많이 쓰임

#1. 수동 리스트 생성 -> 1~10
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('1. 수동 리스트 - ', a, type(a))
'''
1. 수동 리스트 -  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] <class 'list'>
'''

#2. 반복문 > 빈 리스트 생성 > append
b = []
for i in range(1, 11):
    b.append(i);
    
print('2. 자동 리스트 생성 - ', b, type(b))
'''
2. 자동 리스트 생성 -  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] <class 'list'>
'''

#3. list comprehension
c = [i for i in range(1, 11)]
print('3. list comprehension - ', c, type(c))
'''
3. list comprehension -  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] <class 'list'>
'''