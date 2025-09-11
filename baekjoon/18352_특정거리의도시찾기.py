from collections import deque
import sys


def get_input():
    country_cnt, road_cnt, distance, start_country = map(int, sys.stdin.readline().strip().split())

    graph = [[] for _ in range(country_cnt + 1)]

    for _ in range(road_cnt):
        x, y = map(int, sys.stdin.readline().strip().split())

        graph[x].append(y)

    return graph, start_country, distance


def bfs(graph, start_country, distance):
    visited = [-1 for _ in range(len(graph))]
    distance_node = []
    queue = deque([start_country])
    visited[start_country] = 0

    while queue:
        country = queue.popleft()

        for child in graph[country]:
            if visited[child] == -1:
                visited[child] = visited[country] + 1

                if visited[child] == distance:
                    distance_node.append(child)

                queue.append(child)

    if distance_node:
        for node in sorted(distance_node):
            print(node)
        return

    print(-1)


if __name__ == '__main__':
    graph, start_country, distance = get_input()
    bfs(graph=graph, start_country=start_country, distance=distance)