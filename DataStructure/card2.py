# 문제 출처: 백준 2164. 카드2
# 링크 : https://www.acmicpc.net/problem/2164

# 문제
# N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
# 이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
# 예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.
# N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N(1 ≤ N ≤ 500,000)이 주어진다.

# 출력
# 첫째 줄에 남게 되는 카드의 번호를 출력한다.


# 시간 초과 되는 답
# 이슈:
# 파이썬 리스트를 이용한 pop(0) 연산은 첫 번째 요소를 제거하고 나머지 요소들을 한 칸씩 이동시켜야 하기 때문에 리스트의 길이에 따라 성능이 저하될 수 있습니다.
# 큐 라이브러리를 사용한 경우는 내부 구현이 최적화되어 있어 (링크드 리스트 사용 등의 이유로) 큐의 삽입 및 삭제 연산이 빠르게 수행되는 반면,
# 파이썬 리스트를 사용한 경우는 pop(0) 연산이 선형 시간을 소요하여 리스트의 길이가 증가할수록 성능이 저하될 수 있습니다.
def timeout_answer():
    N = int(input())
    cards = [str(x) for x in range(1, N + 1)]

    while len(cards) > 2:
        to_remove = cards[:2]
        cards = cards[2:] + list(to_remove[1])

    if len(cards) > 1:
        print(cards[1])
    else:
        print(cards[0])


# deque는 '덱'이라고 하며 Double Ended Queue의 약자이다. 큐와 스택을 둘 다 만들 수 있는 자료구조인데, 양 끝단에서 모두 push, pop이 가능하다.
# 파이썬에서 collections모듈 안의 deque는 CPython으로 구성되어 있어서 속도면에서 훨씬 빠르다고 한다.
# 일반적인 Queue.Queue는 멀티스레딩을 위한 큐로 사용되어서 이렇게 일반적인 알고리즘 문제를 푸는 데에 있어서는 collections.deque를 사용하는 것이 바람직하다고 한다.
# 그리고 Queue가 내부적으로 collections.deque를 사용한다고 한다.

from collections import deque

N = int(input())
deque = deque([i for i in range(1, N + 1)])

while len(deque) > 1:
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)

print(deque[0])
