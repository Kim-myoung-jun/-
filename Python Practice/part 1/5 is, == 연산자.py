#is, == 연산자
a = 101
b = 100+1
print(a is b) #True 
print(a == b) #True

c = 'korea'
d = 'korea'
print(c is d) #True
print(c == d) #True

e = [1,2,3,4,5] 
f = [1,2,3,4,5] 
print(e is f) #False
print(e == f) #True

'''
101 과 100+1이 a is b 가 True인 이유
 - 다른 언어처럼 메모리에 변수가 들어가는게 아닌 메모리에 값이 들어간다고 이해하면 편함
 101이라는 값이 저장된 메모리 주소를 100+1인 b가 가르킨 것
 
e와 f가 다른 이유는 리스트는 메모리에 따로 만들어짐 그래서 False
'''