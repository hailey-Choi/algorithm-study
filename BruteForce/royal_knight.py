# 출처: 도서 이것이 코딩 테스트다 with python
# Part 2 / Chapter 4 / 실전문제 2 : 왕실의 나이트

# 입력조건: 첫째 줄에 8*8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다.
#         입력문자는 a1처럼 열과 행으로 이뤄진다.
# 출력조건: 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.

# test case:
# input: a1
# output: 2

# 나이트 위치 입력받기
str = input()
x, y = int(str[1]), int(ord(str[0]) - 96)

# 나이트가 이동할 수 있는 모든 경우의 수
count = 8

# 나이트가 이동할 수 있는 모든 방향의 좌표
steps = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, -1), (2, -1), (-2, 1), (2, 1)]

# 좌표 하나씩 확인
for dx, dy in steps:
    # 이동 후 좌표
    nx, ny = x + dx, y + dy
    # 공간을 벗어날 경우 이동할 수 있는 경우에서 빼기
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        count -= 1

print(count)