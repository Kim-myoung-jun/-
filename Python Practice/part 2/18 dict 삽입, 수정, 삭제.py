# 18 dict 삽입, 수정, 삭제

#순서없이 저장 -> 인덱스로 호출 불가능 / key 값을 통해 접근
#key값은 중복 불가, 입력은 가능하나 기존값 변경
#value는 중복가능, 변경도 가능
#데이터 입력을 숫자, 문자 외에도 리스트와 같은 배열 객체로도 입력 가능

#1. 선언
dict_ = {}

#2. 데이터 입력
dict_['id'] = 'hong'
dict_['name'] = '홍길동'
dict_['age'] = 20
dict_['address'] = '서울'

print(dict_)
#{'id': 'hong', 'name': '홍길동', 'age': 20, 'address': '서울'}
print(dict_['name'])
#홍길동

#3. 반복문을 이용한 출력 - key
for i in dict_.keys():
    print(i, end=' ')
#id name age address
#뒤에 ()꼭 써야함
print(' ')

#4. 반복문을 이용한 출력 - value
for i in dict_.values():
    print(i, end=' ')
#hong 홍길동 20 서울
print()

#5. key, value 쌍으로 출력 -> tuple형
for i in dict_.items():
    print(i, end=' ')
#('id', 'hong') ('name', '홍길동') ('age', 20) ('address', '서울')
print()

#6. 빈 dict 선언하기
a = dict()
b = {}
#두 방법 다 동일

#7. 가독성
dict1 = {
    'name': '홍길동',
    'id': 'gdhong',
    'age': 20
}

#8. 중첩 dict ( Nested Dictionary)
dict2 = {
    'name' : '을지문덕',
    'age': 30,
    'pastime': {
        'reading': 30,
        'walking': 60
    }
}
print('dict2 - ', dict2)
#dict2 -  {'name': '을지문덕', 'age': 30, 'pastime': {'reading': 30, 'walking': 60}}

print('nested dict - ', dict2['pastime'])
#nested dict -  {'reading': 30, 'walking': 60}

print('nested dict get value - ', dict2['pastime']['walking'])
#nested dict get value -  60

#9. 삽입, 수정, 삭제
dict3 = {
    'name' : '홍길동',
    'id' : 'gdhong'
}

print('9-1 최초 - ', dict3)
#9-1 최초 -  {'name': '홍길동', 'id': 'gdhong'}

dict3['age'] = 22 #삽입
print('9-2 삽입 - ', dict3)
#9-2 삽입 -  {'name': '홍길동', 'id': 'gdhong', 'age': 22}

dict3['age'] = 33
print('9-3 수정 - ', dict3)
#9-3 수정 -  {'name': '홍길동', 'id': 'gdhong', 'age': 33}

del dict3['age']
print('9-4 삭제 - ', dict3)
#9-4 삭제 -  {'name': '홍길동', 'id': 'gdhong'}