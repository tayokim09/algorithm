import sys
from collections import deque


def get_input():

    test_infos = []
    graph_infos = []

    while True:
        graph_info = []

        start_info = ()
        end_info = ()

        l, r, c = map(int, sys.stdin.readline().strip().split())

        if not l and not r and not c:
            break

        for i in range(l):
            graph_info.append([])

            for j in range(r):
                graph_info[i].append([])
                text = sys.stdin.readline().strip()

                for k in range(c):
                    char = text[k]

                    if char == 'S':
                        start_info = (i, j, k)
                        graph_info[i][j].append(True)
                    elif char == 'E':
                        end_info = (i, j, k)
                        graph_info[i][j].append(True)
                    elif char == '.':
                        graph_info[i][j].append(True)
                    else:
                        graph_info[i][j].append(False)

            sys.stdin.readline()

        test_infos.append((l, r, c, start_info, end_info))
        graph_infos.append(graph_info)

    return test_infos, graph_infos

def is_escape(test_infos, graph_infos):
    for test_info, graph_info in zip(test_infos, graph_infos):
        l, r, c, start, end = test_info
        bfs(l=l, r=r, c=c, start=start, end=end, graph=graph_info)

def bfs(l, r, c, start, end, graph):
    visited = [[[0] * c for _ in range(r)] for _ in range(l)]
    queue = deque()
    queue.append(start)

    while queue:
        z, y, x = queue.popleft()

        if (z, y, x) == end:
            break

        for dx, dy, dz in [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]:
            nx = x + dx
            ny = y + dy
            nz = z + dz

            if 0 <= nz < l and 0 <= ny < r and 0 <= nx < c and not visited[nz][ny][nx] and graph[nz][ny][nx]:
                queue.append((nz, ny, nx))

                visited[nz][ny][nx] = visited[z][y][x] + 1

    z, y, x = end

    if visited[z][y][x]:
        print(f"Escaped in {visited[z][y][x]} minute(s).")
    else:
        print("Trapped!")


if __name__ == '__main__':
    test_infos, graph_infos = get_input()
    is_escape(test_infos=test_infos, graph_infos=graph_infos)