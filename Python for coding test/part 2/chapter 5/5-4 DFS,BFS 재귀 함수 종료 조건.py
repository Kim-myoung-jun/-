# 5-4 DFS,BFS 재귀 함수 종료 조건

def rec(i):
    if i == 100:
        print("종료")
        return
    rec(i+1)
    print(i, "번째에서 종료")
    
rec(0)

# --- 책의 코드 ---
def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀함수에서 ', i+1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')
    
recursive_function(1)