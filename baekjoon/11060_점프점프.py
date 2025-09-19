from collections import deque
import sys


def get_input():
    n = int(sys.stdin.readline().strip())

    jump_cnt = list(map(int, sys.stdin.readline().strip().split()))

    return n, jump_cnt


def bfs(n, jump_cnt):

    if n == 1:
        print(0)
        return

    visited = [-1 for _ in range(n)]
    visited[0] = 0

    queue = deque([0])

    while queue:
        x = queue.popleft()

        for distance in range(1, jump_cnt[x] + 1):
            jump_x = x + distance

            if 0 < jump_x < n and visited[jump_x] == -1:
                visited[jump_x] = visited[x] + 1
                queue.append(jump_x)

    print(visited[-1])


if __name__ == '__main__':
    n, jump_cnt = get_input()
    bfs(n=n, jump_cnt=jump_cnt)