# 24 함수, 함수 호출 파라미터 개수

def my_func(*a):
    n = 0
    for i in a:
        n += i
    return n;

a = my_func(1, 1, 1 ,1)
print(a)
# 4

b = my_func(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(b)
# 45

'''
파라미터를 * 로 받으면 가변길이 파라미터임
튜플로 넘어가짐
'''


#가변길이 입력 파라미터 값들을 함수로 넘겨서 해당 파라미터의 개수와 홀수들의 합 구하는 함수
def odd_func(*a):
    sum = 0
    count = 0
    for i in a:
        count += 1
        if(i%2 != 0):
            sum += i
    
    return sum, count

c = odd_func(1,2,3,4,5,6,7,8,9)
print(c)
#(25, 9)

d = odd_func(1,2,3,4,5,6,7,8,9,10,11)
print(d)
#(36, 11)