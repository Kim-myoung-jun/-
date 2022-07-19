# 20 함수, 리스트, 최고,최저 점수

#10명의 점수 리스트

def max_in_list( lst ):
    return max(lst) #max( ) 함수는 전달받은 리스트내 가장 큰 숫자 반환

def min_in_list( lst):
    return min(lst)

eng = [35, 55, 87, 98, 48, 88, 77, 65, 91, 79]

result = max_in_list( eng )
print( result ) #98

result2 = min_in_list( eng )
print( result2) #35


#최고, 최저 한번에 return
def min_max(lst):
    return min(lst), max(lst)

result3 = min_max(eng)
print(result3, type(result3))
#(35, 98) <class 'tuple'>

#위의 함수로 각각 변수에 넣는법
a, b = min_max(eng)
print('a - ', a, 'b - ', b)
#a -  35 b -  98
