# 7-6 이진 탐색 떡볶이 떡 만들기
n, m = map(int, input().split())
array = list(map(int, input().split()))

#시작점, 끝점 지정
start = 0
end = max(array)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in array:
        # 잘랐을 때의 떡의 양 계산
        if i > mid:
            total += i-mid
    # 떡의 양이 충분한 경우 덜 자르기(중간점 기준 오른쪽 탐색)
    if total >= m:
        result = total #최대한 덜 잘랐을 때가 정답이므로, 여기서 result에 기록
        start = mid + 1
    # 떡의 양이 부족한 경우 더 많이 자르기(중간점 기준 왼쪽으로 탐색)
    else:
        end = mid - 1
        
print(result)