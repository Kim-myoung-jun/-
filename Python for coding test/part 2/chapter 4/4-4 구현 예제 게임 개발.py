# 4-4 구현 예제 게임 개발

n, m = map(int, input().split())
a, b, d = map(int, input().split())

input_map = []

for i in range(n):
  input_map.append(list(map(int, input().split())))

move_steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]

result = 1
count = 0
input_map[a][b] = 2

while True:
  d = d - 1
  if d == -1:
    d = 3
  next_a = a + move_steps[d][0]
  next_b = b + move_steps[d][1]
  if input_map[next_a][next_b] == 0:
    a = next_a
    b = next_b
    result += 1
    input_map[a][b] = 2
    count = 0

  else:
    count += 1
    if count == 4:
      next_a = a + move_steps[d-2][0]
      next_b = b + move_steps[d-2][1]
      if input_map[next_a][next_b] == 1:
        break
      else:
        a = next_a
        b = next_b
        count = 0

print(result)