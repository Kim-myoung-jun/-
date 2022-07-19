# 14 동물, 리스트, 인덱스, 검색

animals = ['elephant', 'hippo', 'lion', 'tiger', 'alligator']

ani_name = input('케이지를 알고 싶은 동물의 이름을 입력해주세요 = ')

ani_index = animals.index(ani_name)
#index()를 쓰면 해당 값에 해당하는 index 번호 리턴

print(f'{ani_name} 동물의 케이지는 {ani_index}번 위치에 있습니다.')
'''
케이지를 알고 싶은 동물의 이름을 입력해주세요 = lion
lion 동물의 케이지는 2번 위치에 있습니다.
'''