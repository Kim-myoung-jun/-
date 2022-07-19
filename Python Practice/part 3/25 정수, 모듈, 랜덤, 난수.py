# 25 정수, 모듈, 랜덤, 난수

# 1. 랜덤 모듈 import
import random

n = random.randint(1, 100)
# 1이상 100미만 사이 랜덤 정수
print(n)
#랜덤 수 나옴

lst = random.sample(range(1, 10), 5)
#1이상 10 미만 사이 랜덤 정수 5개의 리스트 생성
#random.sample()
print(lst)

#로또 생성기
lst2 = random.sample(range(1, 46), 6)
print(lst2)

#ERROR
#err = random.sample(range(1, 10), 10)
#1이상 10 미만의 중복이 없는 수를 뽑아내는데 10개면 중복이 필요해져서 에러가 발생

#random.choice()
#리스트, 튜플, range, 문자열 에서 하나의 요소를 랜덤으로 뽑음
a = random.choice('koreaKOREA')
print(a)

b = random.choice('korea KOREA')
print(b)
    
c = random.choice(['k', 'o', 'r', 'e', 'a', '', 'K', 'O', 'R', 'E', 'A'])
print(c)

#공백도 하나의 문자열로 취급하여 출력 가능함

#d = random.choice( [] ) < error