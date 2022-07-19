# 22 함수, 호추르 파라미터

#함수 호출시 입력 파라미터값을 지정하여 함수를 호출하는 예제
def my_func(id_, name_, strength):
    return id_, name_, strength

result = my_func("id", "name", "str")
print(result, type(result))
#('id', 'name', 'str') <class 'tuple'>
#변수 1개 - 리턴값 여러개 > 튜플 리턴

a, b, c = my_func("aaa", "bbb", "ccc")
print("a - ", a, " b - ", b, " c - ", c, type(a))
#a -  aaa  b -  bbb  c -  ccc <class 'str'>
#변수 n개 - 리턴값 n개 > 각각 할당

'''
d, e = my_func(1, 2, 3)
print(d, e)
 -> Error!!!
'''

