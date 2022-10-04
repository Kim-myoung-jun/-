# 6-7 정렬 위에서 아래로
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort(reverse=True)
for i in range(n):
    print(data[i], end=' ')