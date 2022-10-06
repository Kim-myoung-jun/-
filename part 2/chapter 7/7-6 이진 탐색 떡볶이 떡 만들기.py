# 7-6 이진 탐색 떡볶이 떡 만들기
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in array:
        if i > mid:
            total += i-mid
    if total >= m:
        result = total
        start = mid + 1
    else:
        end = mid - 1
        
print(result)