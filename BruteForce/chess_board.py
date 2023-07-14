# 문제 출처 : 백준 1018. 체스판 다시 칠하기
# 링크 : https://www.acmicpc.net/problem/1018

N, M = map(int, input().split())

# 주어진 보드의 리스트
board = []

# 다시 칠해야 하는 모든 갯수의 리스트
counts = []

for _ in range(N):
    board.append(input())

# 시작점을(i,j)로 두고 8*8 보드 체크
for i in range(N - 7):
    for j in range(M - 7):
        # 시작점이 바뀔때마다 countW, countB 초기화
        # countW는 시작점이 W일때 바꿔야하는 칸의 총 갯수
        # countB는 시작점이 B일때 바꿔야하는 칸의 총 갯수
        countW = 0
        countB = 0
        # 시작점에서부터 8*8 보드 하나씩 체크
        for ii in range(i, i + 8):
            for jj in range(j, j + 8):
                # 짝수 자리일 시 시작 컬러가 같지 않은 경우에 바꿔야하므로 해당 카운트 올려주기
                if (ii + jj) % 2 == 0:
                    if board[ii][jj] != "B":
                        countB += 1
                    if board[ii][jj] != "W":
                        countW += 1
                # 홀수 자리일 시 시작 컬러가 다르지 않은 경우에 바꿔야하므로 해당 카운트 올려주기
                if (ii + jj) % 2 == 1:
                    if board[ii][jj] != "B":
                        countW += 1
                    if board[ii][jj] != "W":
                        countB += 1
        # 최소값 넣어주기
        counts.append(min(countW, countB))

print(min(counts))
