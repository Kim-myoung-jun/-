#다중 변수, 할당, 다중 할당

a = b = c = d = e = 100, 200

print("result - ", a, b, c, d, e)

#result -  (100, 200) (100, 200) (100, 200) (100, 200) (100, 200)
#위는 튜플이다.

print(type(a))
#<class 'tuple'>