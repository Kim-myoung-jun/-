# 그리디 예제 3-1 
#500, 100, 50, 10원짜리 동전이 무한히 있다.
#손님에게 거슬러 줘야할 돈이 N 원일때 거슬러 줘야할 동전의 최소 개수

n = 1260
count = 0
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin
    
print(count)

# 화폐의 종류가 K 개 일때 시간복잡도는 O(K)

#하지만 위의 방법은 만약 800원을 거슬러주고 화폐 단위가 500, 400, 100 인 경우 실패한 알고리즘