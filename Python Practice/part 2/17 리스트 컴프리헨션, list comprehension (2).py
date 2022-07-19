# 17 리스트 컴프리헨션, list comprehension (2)

#괄호 [] 를 사용하지 않고 list() 와 for 문으로 1~10 리스트 만들기
a = list(i for i in range(1, 11))
print('a - ',a, type(a))
'''
a -  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] <class 'list'>
'''

# 1~10 각 숫자 제곱한 리스트
b = [i*i for i in range(1, 11)] #i**2, pow(i, 2) 도 가능
print('b - ', b, type(b))
'''
b -  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] <class 'list'>
'''

# 1~10 각 숫자 제곱, 5의 제곱 제외
c = [i*i for i in range(1, 11) if i != 5 ]
print('c - ', c, type(c))
'''
c -  [1, 4, 9, 16, 36, 49, 64, 81, 100] <class 'list'>
'''

# 1~50 짝수 또는 홀수만 출력
d = [i for i in range(1, 51) if i % 2]
print('d 홀수- ', d, type(d))
'''
d -  [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49] <class 'list'>
'''
d_2 = [i for i in range(1, 51) if i % 2 == 0]
print('d_2 짝수- ', d_2, type(d_2))
'''
d_2 짝수-  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50] <class 'list'>
'''

# 함수 사용
e = [abs(i) for i in [1, 2, -3, 4, 5, -6, 7, 8, -9 ,10]]
print('e 절대값- ', e)
'''
e 절대값-  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''


# 중첩 반복문
f = [(i, j) for i in range(3) for j in range(3)]
print('f - ', f, type(f))
'''
f -  [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)] <class 'list'>
'''
#f = [i, j for i in range(3) for j in range(3)] -> i, j 오류남