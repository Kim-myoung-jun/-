# 5-5 DFS,BFS 팩토리얼
#재귀 미사용
def normal(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(normal(5))


# 재귀 사용
def facto(n):
    if n == 1:
        return 1
    return n * facto(n-1)

print(facto(5))