import sys
from collections import deque


def get_input():
    node_cnt, relation_cnt = map(int, sys.stdin.readline().strip().split())

    graph = {}
    distances = {}
    relations = []

    for _ in range(node_cnt - 1):
        x, y, distance = map(int, sys.stdin.readline().strip().split())

        if x not in graph:
            graph[x] = []

        if y not in graph:
            graph[y] = []

        graph[x].append(y)
        graph[y].append(x)

        distances[(x, y)] = distance
        distances[(y, x)] = distance

    for _ in range(relation_cnt):
        x, y = map(int, sys.stdin.readline().strip().split())
        relations.append((x, y))

    return node_cnt, relations, graph, distances


def get_relation_distance(node_cnt, relations, graph, distances):

    for relation in relations:
        print(bfs(node_cnt=node_cnt, relation=relation, graph=graph, distances=distances))

def bfs(node_cnt, relation, graph, distances):
    visited = [0] * (node_cnt + 1)
    queue = deque()
    queue.append(relation[0])

    while queue:
        x = queue.popleft()

        if x == relation[1]:
            return visited[x]

        for y in graph[x]:

            if not visited[y]:
                visited[y] = visited[x] + distances[(x, y)]
                queue.append(y)


if __name__ == '__main__':
    node_cnt, relations, graph, distances = get_input()
    get_relation_distance(node_cnt=node_cnt, relations=relations, graph=graph, distances=distances)
