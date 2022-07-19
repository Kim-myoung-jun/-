# 15 리스트 중복 제거

lst = ['dog', 'hippo', 'elephant', 'lion', 'alligator', 'hippo', 'lion']

#set() 을 활용

tmp = list(set(lst))
print(tmp)
'''
['dog', 'lion', 'hippo', 'alligator', 'elephant']
집합은 요소가 순서없이 정렬된다.
'''

#에러나는 상황
a = ['dog', 'hippo', 'elephant', 'lion', 'tiger', 'alligator', 'hippo', 'lion']
print(a[3]) #lion 출력

b = set(a)

#print(b[3]) # 에러 발생
print(b)