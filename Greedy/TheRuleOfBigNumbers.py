# Example
# input : 
# 5 8 3
# 2 4 5 4 6
# output:
# 46

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

# 제일 큰 숫자
first = data[n-1]
# 다음으로 큰 숫자
second = data[n-2]

# first가 더해지는 횟수
countFirst = (m // (k+1)) * k + (m % (k+1))
# second가 더해지는 횟수
countSecond = m - countFirst

result = first * countFirst + second * countSecond

print(result)
