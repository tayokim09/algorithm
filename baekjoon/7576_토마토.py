from collections import deque
import sys


def get_input():
    width, height = map(int, sys.stdin.readline().strip().split())
    graph = []
    tomato_position = []

    for i in range(height):
        graph.append(list(map(int, sys.stdin.readline().strip().split())))

        for j in range(width):
            if graph[i][j] == 1:
                tomato_position.append((j, i))

    return width, height, graph, tomato_position


def bfs(width, height, graph, tomato_position):
    queue = deque()
    queue.extend(tomato_position)

    while queue:
        x, y = queue.popleft()

        for dx, dy in[(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < width and 0 <= ny < height and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((nx, ny))

    max_day = 0

    for row in graph:
        for i in row:
            if i == 0:
                print(-1)
                return
            else:
                max_day = max(max_day, i)

    print(max_day - 1)


if __name__ == '__main__':
    width, height, graph, tomato_position = get_input()
    bfs(width=width, height=height, graph=graph, tomato_position=tomato_position)