import sys
input = sys.stdin.readline
INF = int(1e9)
node, edge = map(int, input().split())
arr = [[INF]*(node+1) for _ in range(node+1)]

for i in range(edge):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
for i in range(1, node+1):
    for j in range(1, node+1):
        if a == b:
            arr[a][b] = 0

for k in range(1, node+1):
    for i in range(1, node+1):
        for j in range(1, node+1):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

x, k = map(int, input().split())
distance = arr[1][k] + arr[k][x]
if distance == INF:
    print(-1)
else:
    print(distance)