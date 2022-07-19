# 29 알고리즘

#리스트에서 최고값 출력, max()함수 사용 불가

def max_in_list(lst):
    first_max_num = lst[0]
    
    for i in lst[1:]: #1번 인덱스 부터
        if(i > first_max_num):
            first_max_num = i
            
    return first_max_num

lst = [28,24,74,37,83,54,71,17]

print(max_in_list(lst))
#83
print(max(lst))
#83

