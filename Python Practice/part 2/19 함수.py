# 19 함수

#1. 함수 작성
def a():
    print('붕어빵')
    
def b():
    print('개구리빵')

#() 뒤에 : 잊지말기
#들여쓰기 중요, tab이나 space 4칸

#2. 함수 호출
a()
b()
'''
붕어빵
개구리빵
'''

#3. 리턴 함수
def c():
    str = '슈크림빵'
    return str

print('c() - ', c())
#c() -  슈크림빵