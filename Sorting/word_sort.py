# 문제 출처: 백준 1181. 단어 정렬
# 링크 : https://www.acmicpc.net/problem/1181

n = int(input())
lst = []

# 입력받은 단어들을 리스트에 저장
for i in range(n):
    lst.append(input())

# 중복 단어 빼기
set_lst = set(lst)
lst = list(set_lst)

# 사전 순으로 정렬후 길이 순으로 정렬
lst.sort()
lst.sort(key=len)

for i in lst:
    print(i)
