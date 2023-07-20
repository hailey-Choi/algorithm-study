# 출처: 도서 이것이 코딩 테스트다 with python
# Part 2 / Chapter 5 / 5-8.py DFS 예제


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)


# Given adjacency list
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

visited = [False] * len(graph)

dfs(graph, 1, visited)
