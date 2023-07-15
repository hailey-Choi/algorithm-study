# 문제 출처: 백준 1259. 팰린드롬수
# 링크 : https://www.acmicpc.net/problem/1259

while True:
    num = input()
    if num == "0":
        break

    if num == num[::-1]:
        print("yes")
    else:
        print("no")
