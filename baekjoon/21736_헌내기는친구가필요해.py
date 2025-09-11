from collections import deque
import sys


def get_input():
    height, width = map(int, sys.stdin.readline().strip().split())
    x, y = 0, 0
    graph = []

    for i in range(height):
        graph.append(list(sys.stdin.readline().strip()))

        for j in range(width):
            if graph[i][j] == 'I':
                x, y = i, j

    return graph, x, y, height, width


def bfs(graph, x, y, height, width):
    visited = [[0] * (width) for _ in range(height)]
    people_cnt = 0
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + dx < height and 0 <= y + dy < width and visited[x + dx][y + dy] == 0:
                visited[x + dx][y + dy] += 1

                if graph[x + dx][y + dy] == 'X':
                    continue

                if graph[x + dx][y + dy] == 'P':
                    people_cnt += 1

                queue.append((x + dx, y + dy))

    if people_cnt:
        print(people_cnt)
        return

    print('TT')


if __name__ == '__main__':
    graph, x, y, height, width = get_input()
    bfs(graph=graph, x=x, y=y, height=height, width=width)