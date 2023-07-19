# 출처: 도서 이것이 코딩 테스트다 with python
# Part 2 / Chapter 4 / 실전문제 3 : 게임 개발


def countVisits(x, y, dir, gamespace):
    # 북동남서 방향을 기준으로 좌표 이동
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    # 방문했던 칸을 저장해둘 리스트
    visited = [[0 for _ in range(M)] for _ in range(N)]
    # 현재 좌표 방문 처리
    visited[x][y] = 1

    def turn_left(dir):
        if dir == 0:
            dir += 3
        else:
            dir -= 1

    # 1. 현재 위치에서 현재 방향을 기준으로 왼쪽방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈곳을 정함
    # 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한칸을 전진함
    #    왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아감
    # 3. 만약 네 방향 모두 이미 가본 칸이거나 바다 인 경우, 바라보는 방향을 유지한 채로 한 칸 뒤로가고 1단계로 돌아감
    #    단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춤

    visit_count = 1
    turn_count = 0
    # 시뮬레이션 시작
    while True:
        turn_left(dir)
        # 왼쪽 방향 칸이 육지이거나 가본 적 없는 칸일 경우
        if (
            gamespace[x + dx[dir]][y + dy[dir]] == 0
            or visited[x + dx[dir]][y + dy[dir]] == 0
        ):
            x += dx[dir]
            y += dy[dir]
            visited[x][y] = 1
            visit_count += 1
            turn_count = 0
            continue
        # 왼쪽 방향 칸이 바다이거나 이미 가본 칸일 경우
        else:
            turn_count += 1
        # 네 방향 모두 이미 가본 칸이거나 바다 인 경우
        if turn_count == 4:
            # 뒤쪽 방향이 육지인 칸인 경우
            if gamespace[x - dx[dir]][y - dy[dir]] == 0:
                x -= dx[dir]
                y -= dy[dir]
                turn_count = 0
            # 뒤쪽 방향이 바다인 칸인 경우
            else:
                break
            turn_count = 0

    return visit_count


if __name__ == "__main__":
    N, M = map(int, input().split())
    x, y, dir = map(int, input().split())
    gamespace = []

    for _ in range(N):
        gamespace.append(list(map(int, input().split())))

    print(countVisits(x, y, dir, gamespace))
