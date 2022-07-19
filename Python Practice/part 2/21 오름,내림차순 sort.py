# 21 오름,내림차순 sort
#sort() sorted() 차이

lst = [100, 40, 70, 90, 60]

#sort()나 sorted()는 기본 오름차순
lst.sort()
print(lst)
#[40, 60, 70, 90, 100]

lst.sort(reverse=True)
print(lst)
#[100, 90, 70, 60, 40]

#-----------------------------------

#lst.sorted() <- Error
#sorted() 는 변수에 저장되어야 함

a = sorted(lst)
print('a - ', a)
print('lst - ', lst)
#a - [40, 60, 70, 90, 100]
#lst - [100, 90, 70, 60, 40]
#sorted()는 원본 리스트의 정렬을 유지하고 정렬된 값만 변수에 저장됨

b = sorted(a, reverse=True)
print('a - ', a)
print('b - ', b)
#a -  [40, 60, 70, 90, 100]
#b -  [100, 90, 70, 60, 40]

c = lst.sort()
print(c)
#None