import sys
from collections import deque


def get_input():

    n, k = map(int, sys.stdin.readline().strip().split())

    graph = []
    virus_position = []

    for nx in range(n):
        row = list(map(int, sys.stdin.readline().strip().split()))
        graph.append(row)

        for ny in range(n):
            if row[ny] > 0:
                virus_position.append((nx, ny, row[ny], 0))

    virus_position = sorted(virus_position, key=lambda x: x[2])

    s, y, x = map(int, sys.stdin.readline().strip().split())

    return virus_position, (x, y, s), graph, n


def bfs(virus_position, finish_position, graph, n):
    queue = deque()
    queue.extend(virus_position)

    while queue:
        y, x, virus, sec = queue.popleft()

        if sec == finish_position[2]:
            break

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n and not graph[ny][nx]:
                graph[ny][nx] = virus
                queue.append((ny, nx, virus, sec + 1))

    print(graph[finish_position[1] - 1][finish_position[0] - 1])


if __name__ == '__main__':
    virus_position, finish_position, graph, n = get_input()
    bfs(virus_position, finish_position, graph, n)