from collections import deque
import sys


def get_input():
    height, width = map(int, sys.stdin.readline().strip().split())
    graph = []

    for i in range(height):
        graph.append(list(map(int, sys.stdin.readline().strip().split())))

    return width, height, graph


def get_max_distance(width, height, graph):
    max_distance = 0

    for i in range(height):
        for j in range(width):
            if graph[i][j] == 0:
                max_distance = max(max_distance, bfs(width=width, height=height, x=j, y=i, graph=graph))

    print(max_distance)


def bfs(width, height, x, y, graph):
    visited = [[-1] * width for _ in range(height)]
    visited[y][x] = 0
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for dx, dy in[(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1), (1, 1), (-1, -1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < width and 0 <= ny < height:
                if visited[ny][nx] == -1:
                    visited[ny][nx]  = visited[y][x] + 1
                    queue.append((nx, ny))

                    if graph[ny][nx] == 1:
                        return visited[ny][nx]

    return 0


if __name__ == '__main__':
    width, height, graph = get_input()
    get_max_distance(width=width, height=height, graph=graph)