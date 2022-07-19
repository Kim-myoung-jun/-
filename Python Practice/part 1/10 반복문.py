# 10 반복문

for i in range(10):
    print(i)
    
#0~9가 0 1 2 3 4 5 6 7 8 9 (옆으로 나오게) 출력
for i in range(10):
    print(i, end=' ')
    
print()#결과창 줄바꿈용

#0, 1, 2..., 8, 9 (마지막 , 안나오게)
for i in range(10):
    if i<9:
        print(i, end=', ')
    else:
        print(i)
        
# 4~21 홀수 합
sum = 0
for i in range(4, 22):
    if i%2 == 1:
        sum += i

print(sum)
    
    
#1~100 짝수만 출력
for i in range(1, 101):
    if i%2 == 0:
        print(i, end=' ')
      
print( )
  
for i in range(2, 101, 2):
    print(i, end=' ')
    
print()
#2단~9단 구구단 출력 
for i in range(2, 10):
    for j in range(1, 10):
        print(i, ' x ', j, ' = ', i*j)
# (옆으로)
for i in range(1, 10):
    for j in range(2, 10):
        print(j, ' x ', i, ' = ', j*i, end=' ')
    print()
    
print()

#리스트 요소 출력, 가로로
lst = ['dog', 'hippo', 'elephant', 'lion', 'tiger', 'alligator']

for i in range(len(lst)):
    print(lst[i], end=' ')
    
print()

#리스트 거꾸로 출력
for i in lst[ : : -1]: #[ start : last : step] <- step = -1 이어서 거꾸로 한칸씩 (-2이면 거꾸로 2칸씩)
    #print(lst[i], end=' ') <- range() 를 쓴게 아닌 lst를 직접 사용했기 때문에 i에 배열 값이 직접 들어간다.
    print(i, end=' ')
    

"""
0
1
2
3
4
5
6
7
8
9
0 1 2 3 4 5 6 7 8 9
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
117
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 
86 88 90 92 94 96 98 100
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 
86 88 90 92 94 96 98 100
2  x  1  =  2
2  x  2  =  4
2  x  3  =  6
2  x  4  =  8
2  x  5  =  10
2  x  6  =  12
2  x  7  =  14
2  x  8  =  16
2  x  9  =  18
3  x  1  =  3
3  x  2  =  6
3  x  3  =  9
3  x  4  =  12
3  x  5  =  15
3  x  6  =  18
3  x  7  =  21
3  x  8  =  24
3  x  9  =  27
4  x  1  =  4
4  x  2  =  8
4  x  3  =  12
4  x  4  =  16
4  x  5  =  20
4  x  6  =  24
4  x  7  =  28
4  x  8  =  32
4  x  9  =  36
5  x  1  =  5
5  x  2  =  10
5  x  3  =  15
5  x  4  =  20
5  x  5  =  25
5  x  6  =  30
5  x  7  =  35
5  x  8  =  40
5  x  9  =  45
6  x  1  =  6
6  x  2  =  12
6  x  3  =  18
6  x  4  =  24
6  x  5  =  30
6  x  6  =  36
6  x  7  =  42
6  x  8  =  48
6  x  9  =  54
7  x  1  =  7
7  x  2  =  14
7  x  3  =  21
7  x  4  =  28
7  x  5  =  35
7  x  6  =  42
7  x  7  =  49
7  x  8  =  56
7  x  9  =  63
8  x  1  =  8
8  x  2  =  16
8  x  3  =  24
8  x  4  =  32
8  x  5  =  40
8  x  6  =  48
8  x  7  =  56
8  x  8  =  64
8  x  9  =  72
9  x  1  =  9
9  x  2  =  18
9  x  3  =  27
9  x  4  =  36
9  x  5  =  45
9  x  6  =  54
9  x  7  =  63
9  x  8  =  72
9  x  9  =  81
2  x  1  =  2 3  x  1  =  3 4  x  1  =  4 5  x  1  =  5 6  x  1  =  6 7  x  1  =  7 8  x  1  =  8 9  x  1  =  9
2  x  2  =  4 3  x  2  =  6 4  x  2  =  8 5  x  2  =  10 6  x  2  =  12 7  x  2  =  14 8  x  2  =  16 9  x  2  =  18      
2  x  3  =  6 3  x  3  =  9 4  x  3  =  12 5  x  3  =  15 6  x  3  =  18 7  x  3  =  21 8  x  3  =  24 9  x  3  =  27 
2  x  4  =  8 3  x  4  =  12 4  x  4  =  16 5  x  4  =  20 6  x  4  =  24 7  x  4  =  28 8  x  4  =  32 9  x  4  =  36    
2  x  5  =  10 3  x  5  =  15 4  x  5  =  20 5  x  5  =  25 6  x  5  =  30 7  x  5  =  35 8  x  5  =  40 9  x  5  =  45 
2  x  6  =  12 3  x  6  =  18 4  x  6  =  24 5  x  6  =  30 6  x  6  =  36 7  x  6  =  42 8  x  6  =  48 9  x  6  =  54   
2  x  7  =  14 3  x  7  =  21 4  x  7  =  28 5  x  7  =  35 6  x  7  =  42 7  x  7  =  49 8  x  7  =  56 9  x  7  =  63 
2  x  8  =  16 3  x  8  =  24 4  x  8  =  32 5  x  8  =  40 6  x  8  =  48 7  x  8  =  56 8  x  8  =  64 9  x  8  =  72 
2  x  9  =  18 3  x  9  =  27 4  x  9  =  36 5  x  9  =  45 6  x  9  =  54 7  x  9  =  63 8  x  9  =  72 9  x  9  =  81   

dog hippo elephant lion tiger alligator
alligator tiger lion elephant hippo dog
"""