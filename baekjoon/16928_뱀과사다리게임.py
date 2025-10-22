from collections import deque
import sys


def get_input():
    ladder_cnt, snake_cnt = map(int, sys.stdin.readline().strip().split())
    graph = {}

    for _ in range(ladder_cnt):
        x, y = map(int, sys.stdin.readline().strip().split())

        graph[x] = y

    for _ in range(snake_cnt):
        x, y = map(int, sys.stdin.readline().strip().split())

        graph[x] = y

    return graph


def bfs(graph):
    visited = [False * 100 for i in range(100)]
    queue = deque()
    queue.extend([(1, 0)])

    while queue:
        x, cnt = queue.popleft()

        for i in range(1, 7):
            y = graph[x + i] if x + i in graph else x + i

            if y == 100:
                print(cnt + 1)
                return

            if not visited[y] and y <= 100:
                visited[y] = True
                queue.append((y, cnt+1))


if __name__ == '__main__':
    graph = get_input()
    bfs(graph=graph)