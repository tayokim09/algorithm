from collections import deque
import sys


def get_input():
    subin, sister = map(int, sys.stdin.readline().strip().split())

    return subin, sister


def bfs(subin, sister):
    visited = [0] * 100001
    queue = deque([subin])
    visited[subin] = 1

    while queue:
        x = queue.popleft()

        if x == sister:
            break

        if 0 <= x * 2 <= 100000 and not visited[x * 2]:
            visited[x * 2] = visited[x]
            queue.appendleft(x * 2)

        if 0 <= x - 1 <= 100000 and not visited[x - 1]:
            visited[x - 1] = visited[x] + 1
            queue.append(x - 1)

        if 0 <= x + 1 <= 100000 and not visited[x + 1]:
            visited[x + 1] = visited[x] + 1
            queue.append(x + 1)

    print(visited[sister] - 1)


if __name__ == '__main__':
    subin, sister = get_input()
    bfs(subin=subin, sister=sister)