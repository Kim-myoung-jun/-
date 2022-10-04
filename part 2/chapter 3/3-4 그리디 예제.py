# 그리디 예제 3-4
# 1이 될 때까지

'''
1. N에서 1을 뺀다.
2. N을 K로 나눈다(N이 K로 나누어 떨어질때만)
첫째 줄에 N(2<= N <= 100000)과 K(2<= k <= 100000)가 공백으로 구분되며 각각 자연수로 주어진다.
이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.

첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야하는 횟수의 최솟값을 출력한다.

25 5
2
'''
n, k = map(int, input().split())
count = 0

while(True):
    a = n // k
    b = n - (a * k)
    
    if a >= k:
        count += 1 + b
        n = a
        
    if a < k:
        count += b + 1
        break
    
if a != 1:
    count += a - 1
            
print(count)