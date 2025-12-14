import sys
from collections import deque


def get_input():
    width, height = map(int, sys.stdin.readline().strip().split())

    graph = [[] for _ in range(height)]
    stuff = {}
    stuff_cnt = 0
    start = tuple()

    for h in range(height):
        structures = sys.stdin.readline().strip()

        for w in range(width):
            structure = structures[w]

            if structure == 'S':
                start = (h, w)

            elif structure == 'X':
                stuff[(h, w)] = stuff_cnt
                stuff_cnt += 1

            graph[h].append(structure)

    return width, height, graph, stuff, stuff_cnt, start

def bfs(width, height, graph, stuff, stuff_cnt, start):

    visited = [[[-1 for _ in range(1 << stuff_cnt)] for _ in range(width)] for _ in range(height)]
    visited[start[0]][start[1]][0] = 0

    queue = deque()
    queue.append((start[0], start[1], 0))


    while queue:
        h, w, state = queue.popleft()

        if graph[h][w] == 'E' and state == (1 << stuff_cnt) - 1:
            print(visited[h][w][state])
            break

        for dh, dw in[(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nh = h + dh
            nw = w + dw

            if 0 <= nh < height  and 0 <= nw < width and graph[nh][nw] != '#' and visited[nh][nw][state] == -1:
                if graph[nh][nw] == 'X':
                    nstate = state | (1 << stuff[(nh, nw)])
                else:
                    nstate = state

                visited[nh][nw][nstate] = visited[h][w][state] + 1
                queue.append((nh, nw, nstate))


if __name__ == '__main__':
    width, height, graph, stuff, stuff_cnt, start = get_input()
    bfs(width=width, height=height, graph=graph, stuff=stuff, stuff_cnt=stuff_cnt, start=start)
