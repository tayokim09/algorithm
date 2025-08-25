from collections import deque
import sys

def get_input():
    node_cnt = int(input())
    graph = [[] for _ in range(node_cnt + 1)]

    for _ in range(node_cnt - 1):
        x, y = map(int, sys.stdin.readline().strip().split())

        graph[x].append(y)
        graph[y].append(x)

    return graph


def bfs(graph):
    visited = [0 for _ in range(len(graph))]
    queue = deque([1])

    while queue:
        parent = queue.popleft()

        for child in graph[parent]:
            if not visited[child]:
                visited[child] = parent
                queue.append(child)

    for i in range(2, len(visited)):
        print(visited[i])

if __name__ == '__main__':
    graph = get_input()
    bfs(graph=graph)
