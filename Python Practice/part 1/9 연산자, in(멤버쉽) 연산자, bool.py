# 9 연산자, in(멤버쉽) 연산자, bool
# + - * / // ** %
# // -> 몫
# % -> 나머지
# ** 제곱, **3 -> 3제곱, **4 -> 4제곱

a = 3
print(a**3) # -> 27

#in(멤버쉽) 연산자
#리스트, 튜플 등에서 내부에 해당 값이 있는지 확인하는 기능

lst = [1, 2, 3, 4, 5]
a = 100 in lst
print(a) #-> False

tpl = 1, 2, 3, 4
b = 4 in tpl
print(b) #-> True

#bool 연산자
print( bool(1) ) # True
print( bool(0) ) # False
#print( bool(none) ) #Error
print( bool(None) ) #False, 대문자로 써야함
