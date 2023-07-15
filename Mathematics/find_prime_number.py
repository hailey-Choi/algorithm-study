# 문제 출처: 백준 1978. 소수 찾기
# 링크: https://www.acmicpc.net/problem/1978

# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

N = int(input())
nums = map(int, input().split())
count = 0

for n in nums:
    if n <= 1:
        continue
    divisible_num = 0
    for x in range(2, n):
        if n % x == 0:
            divisible_num += 1
    if divisible_num == 0:
        count += 1

print(count)
