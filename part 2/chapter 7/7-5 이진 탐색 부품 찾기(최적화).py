# 7-5 이진 탐색 부품 찾기(최적화)
n = int(input())
data1 = list(map(int, input().split()))
m = int(input())
data2 = list(map(int, input().split()))

for i in data2:
    if i in data1:
        print("yes", end=' ')
    else:
        print("no", end=' ')