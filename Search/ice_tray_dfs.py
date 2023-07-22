# 출처: 도서 이것이 코딩 테스트다 with python
# Part 2 / Chapter 5 / 실전문제 3. 음료수 얼려먹기

N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))


def dfs(x, y):
    # 종료조건 1: 얼음 틀을 벗어남
    if x < 0 or x > N - 1 or y < 0 or y > M - 1:
        return False

    # 성공조건: 얼음칸의 값이 0일 경우
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True

    # 종료조건 2: 얼음칸의 값이 1일 경우
    return False


count = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            count += 1

print(count)
