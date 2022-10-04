# 구현 예제 4-1
'''
상하좌우

N x N 크기의 정사각형 공간
좌표 (1, 1)부터 시작 L R U D를 입력받아 도착하는 지점을 찾는다.
예를 들어 (1, 1)지점에서 L U를 입력받으면 공간을 벗어나므로 무시된다.

입력 조건
첫째 줄에 공간의 크기를 나타내는 N이 주어진다. (1 <= N <= 100)
둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1 <= 이동 횟수 <= 100)

출력 조건
첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (x, y)를 공백으로 구분하여 출력한다.

5
R R R U D D

3 4
'''

n = int(input())
x, y = 1, 1
plans = input().split()

for plan in plans:
    if plan == "L" and y>1:
        y -= 1
    elif plan == "R" and y<n:
        y += 1
    elif plan == "U" and x>1:
        x -= 1
    elif plan == "D" and x<n:
        x += 1

print(x, y)