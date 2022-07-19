#is, 연산자, 결과, print
a = "korea"
b = "korea"
print('a is b - ', a is b)

b += "!"
print('a is b - ', a is b)

c = b[:-1] #slice, !를 지워서 c = "korea"다.
print('a is c - ', a is c)
'''
a is b -  True
a is b -  False
a is c -  False

문자열은 True
b 는 korea! 이니까 당연히 false
c 는 slice한 값이여서 a와 같은 korea여도 새로운 주소에 할당된다
'''