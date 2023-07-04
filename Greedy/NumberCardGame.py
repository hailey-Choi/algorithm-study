# 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 자연수로 주어진다.
# 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10,000이하의 자연수이다.
# 첫째 줄에 게임의룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.
# 게임의 룰: 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야함; 최정적으로 가장 높은 숫자를 뽑아야함

# Example
# Input: 
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2 
# Output: 2

n, m = map(int, input().split())
result = 0 

for i in range(n):
    data = list(map(int, input().split()))
    temp = min(data)
    if result < temp: # max()를 이용해 비교하는 방법도 있음
      result = temp 
print(result)
