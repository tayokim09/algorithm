import sys
from collections import deque


def get_input():
    height, width = map(int, sys.stdin.readline().strip().split())

    graph = [[] for _ in range(height)]
    ground_points = []

    for h in range(height):
        line = sys.stdin.readline().strip()

        for w in range(width):
            is_ground = line[w] == 'L'
            graph[h].append(is_ground)
            if is_ground:
                ground_points.append((h, w))

    return height, width, graph, ground_points

def get_treasure_distance(height, width, graph, ground_points):

    distance = 0
    for h, w in ground_points:
        distance = max(bfs(height=height, width=width, graph=graph, x=w, y=h), distance)

    print(distance)

def bfs(height, width, graph, x, y):
    visited = [[False] * width for _ in range(height)]
    queue = deque()
    queue.extend([(x, y, 1)])
    visited[y][x] = True
    distance = 0

    while queue:
        x, y, dist = queue.popleft()

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < width and 0 <= ny < height and not visited[ny][nx] and graph[ny][nx]:
                distance = max(distance, dist)
                queue.append((nx, ny, dist + 1))
                visited[ny][nx] = True

    return distance

if __name__ == '__main__':
    height, width, graph, ground_points = get_input()
    get_treasure_distance(height=height, width=width, graph=graph, ground_points=ground_points)
