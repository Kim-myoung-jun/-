#다중 할당, 여러변수, 값
#다중할당시 여러 개의 값을 여러 개의 변수에 각각 저장시키는 코드를 한줄로 작성

a, b, c, d = 100, 3.14, 'k', 'korea'

print("result - ", a, b, c, d)
#result -  100 3.14 k korea

a = 100, 3.14, 'k', 'korea'
print("a - ", a, type(a))
#a -  (100, 3.14, 'k', 'korea') <class 'tuple'>
# 위에도 튜플임