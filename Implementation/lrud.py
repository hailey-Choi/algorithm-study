# 출처: 도서 이것이 코딩 테스트다 with python - Part 2. 예제 4-1 상하좌우

# 입력조건:
# - 첫째 줄에 공간의 크기를 나타내는 N이 주어진다. (1 <= N <= 100)
# - 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1 <= 이동 횟수 <= 100)
# 출력조건:
# 첫째줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X,Y)를 공백으로 구분하여 출력한다.

# test case:
# input:
# 5
# R R R U D D
# output:
# 3 4

n = int(input())
plans = input().split()
x, y = 1, 1

# L, R, U, D 에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if move_types[i] == plan:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > 100 or ny > 100:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
