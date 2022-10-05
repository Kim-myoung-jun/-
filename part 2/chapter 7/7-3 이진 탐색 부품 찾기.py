# 7-3 이진 탐색 부품 찾기
n = int(input())
data1 = list(map(int, input().split()))
data1.sort()
m = int(input())
data2 = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return "no"
    mid = (start + end) // 2
    if array[mid] == target:
        return "yes"
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


for i in range(m):
    print(binary_search(data1, data2[i], 0, n-1), end=' ')