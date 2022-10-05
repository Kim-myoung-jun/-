# 7-4 이진 탐색 부품 찾기(반복문)
n = int(input())
data1 = list(map(int, input().split()))
data1.sort()
m = int(input())
data2 = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return "yes"
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
            
    return "no"

for i in data2:
    print(binary_search(data1, i, 0, n-1), end=' ')