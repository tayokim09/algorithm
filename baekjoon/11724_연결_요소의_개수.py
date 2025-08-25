from collections import deque
import sys

def get_input():
    point_cnt, edge_cnt = map(int, input().split(' '))
    graph = {i: [] for i in range(1, point_cnt + 1)}

    for _ in range(edge_cnt):
        x, y = map(int, sys.stdin.readline().strip().split())

        graph[x].append(y)
        graph[y].append(x)
    return point_cnt, graph


def bfs(point_cnt, graph):
    visited = [0 for _ in range(point_cnt + 1)]
    connect_cnt = 0

    for start in range(1, point_cnt + 1):
        if visited[start]:
            continue

        queue = deque([start])

        while queue:
            point = queue.popleft()

            if not visited[point]:
                visited[point] = 1
                queue.extend(graph[point])

        connect_cnt += 1

    print(connect_cnt)

if __name__ == '__main__':
    point_cnt, graph = get_input()
    bfs(point_cnt=point_cnt, graph=graph)

