# 6-8 정렬 성적이 낮은 순서로 학생 출력하기
n = int(input())
data = {}
for _ in range(n):
    input_data = input().split()
    data[input_data[0]] = int(input_data[1])
    
sorted_data = sorted(data.items(), key=lambda item: item[1])  
#print(sorted_data)
for i in sorted_data:
    print(i[0], end=' ')
    
#정답 코드
n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))
    
array = sorted(array, key = lambda student: student[1])

for student in array:
    print(student[0], end=' ')