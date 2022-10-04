# 그리디 예제 3-2
#큰 수의 법칙
#첫째 줄에 N, M, K 자연수가 주어진다 (각 자연수는 공백으로 구분)
#둘째 줄에 N개의 자연수가 주어진다(공백으로 구분)
#주어진 수들을 M번 더하며, 배열의 특정 인덱스에 해당하는 수가 연속으로 K번을 초과해서 더해질 수 없다.

# 5 8 3
# 2 4 5 4 6
# 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 46
# 총 8번 더해지며, 6이 3번 나오자 그 다음 큰 수인 5가 더해지고 다시 6이 세번 더해진 것

# 5 7 2
# 3 4 3 4 3
# 4+4+4+4+4+4+4 = 28

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if(m == 0):
            break
        result += first
        m -= 1
    
    if(m==0):
        break
    
    result += second
    m -= 1
    
print(result)