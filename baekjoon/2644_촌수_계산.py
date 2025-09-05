from collections import deque
import sys


def get_input():
    people_cnt = int(sys.stdin.readline().strip())
    first, second = map(int, sys.stdin.readline().strip().split())
    relation_cnt = int(sys.stdin.readline().strip())

    graph = [[] for _ in range(people_cnt + 1)]

    for _ in range(relation_cnt):
        x, y = map(int, sys.stdin.readline().strip().split())

        graph[x].append(y)
        graph[y].append(x)

    return graph, first, second


def bfs(graph, first, second):
    visited = [0 for _ in range(len(graph))]
    queue = deque([first])

    while queue:
        parent = queue.popleft()

        if parent == second:
            print(visited[second])
            return

        for child in graph[parent]:
            if not visited[child]:
                visited[child] = visited[parent] + 1
                queue.append(child)

    print(-1)


if __name__ == '__main__':
    graph, first, second = get_input()
    bfs(graph=graph, first=first, second=second)