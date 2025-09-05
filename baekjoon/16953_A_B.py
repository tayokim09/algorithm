from collections import deque
import sys


def get_input():
    first, second = map(int, sys.stdin.readline().strip().split())

    return first, second


def bfs(first, second):
    queue = deque([(first, 1)])

    while queue:
        value, cnt = queue.popleft()

        if value == second:
            print(cnt)
            return

        if value <= second:
            queue.append((value * 2, cnt + 1))

        if value <= second:
            queue.append((value * 10 + 1, cnt + 1))

    print(-1)


if __name__ == '__main__':
    first, second = get_input()
    bfs(first=first, second=second)