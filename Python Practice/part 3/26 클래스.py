# 26 클래스

#[1]: 변수
print("[변수를 사용한 캐릭터 정보 출력]")

person1_name = '홍길동'
person1_age = 20
person1_power = 7

person2_name = '이순신'
person2_age = 30
person2_power = 9

print(f'선택 - {person1_name} 나이 - {person1_age} 파워 - {person1_power}')
print(f'선택 - {person2_name} 나이 - {person2_age} 파워 - {person2_power}')
'''
[변수를 사용한 캐릭터 정보 출력]
선택 - 홍길동 나이 - 20 파워 - 7
선택 - 이순신 나이 - 30 파워 - 9
'''

#[2]: 리스트 / 딕셔너리 사용
print('[리스트를 사용한 정보 출력]')
person1 = ['홍길동', 20, 7]
person2 = ['이순신', 30, 9]

print(f'선택 - {person1[0]} 나이 - {person1[1]} 파워 - {person1[2]}')
print(f'선택 - {person2[0]} 나이 - {person2[1]} 파워 - {person2[2]}')
'''
[리스트를 사용한 정보 출력]
선택 - 홍길동 나이 - 20 파워 - 7
선택 - 이순신 나이 - 30 파워 - 9
'''

#[3] 각 개릭터의 파워 랜덤으로
import random

def add_power(id):
    id[2] = random.choice(range(1, 10))
    return id

print('[함수와 리스트를 사용한 정보 출력]')

print(add_power(person1), add_power(person2))
'''
[함수와 리스트를 사용한 정보 출력]
['홍길동', 20, 4] ['이순신', 30, 4]
power 부분이 랜덤으로 변경됨
'''


#[4] 클래스 생성
# 클래스 사용하면 변수와 함수를 하나로 묶어서 더 효율적
#클래스 멤버 -> 변수, 메서드
#메서드 -> 클래스의 행위나 동작을 구현 > 함수 -> 클래스에서는 메서드라고 호칭함

#클래스 작성
# 1 - 클래스 작성 -> class 키워드로 선언하고 클래스명 지정
# 2 - 클래스 이름 -> CamelCase 사용
# 3 - 함수가 아니기 때문에 ()를 사용하지 않고 : 을 붙여 종료
# 4 - 클래스 선언과 클래스 명만 지정하고 내용은 pass 설정만 해놓아도 하나의 클래스가 만들어진것
class testClass:
    pass # - 테스트시 많이 사용, 없으면 에러



#[5] 클래스 사용

print('[클래스 사용]')
test = testClass()
print(test, type(test))
'''
[클래스 사용]
<__main__.testClass object at 0x0000029DD9BB4320> <class '__main__.testClass'>
'''

class PersonInfo:
    def hello(self):
        print('Hello')
        
p = PersonInfo()
print(p, type(p))
'''
<__main__.PersonInfo object at 0x0000029DD9E1A2B0> <class '__main__.PersonInfo'>
'''
p.hello()
'''
Hello
'''