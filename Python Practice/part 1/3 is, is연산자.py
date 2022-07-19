#is, is연산자
a = [1, 2, 3, 4, 5]
b = a
c = [1, 2, 3, 4, 5]

print('a is b = ', a is b)
print('a is c = ', a is c)
'''
a is b =  True
a is c =  False
주소 차이로 false
is연산자는 == 처럼 데이터 값 비교가 아닌 같은 객체를 가리키는지 비교
'''